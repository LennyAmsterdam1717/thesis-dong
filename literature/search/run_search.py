#!/usr/bin/env python3
"""Run the R1-R4 searches of literature/search-plan.md against arXiv and OpenAlex.

Standard library only. Usage:
    python run_search.py --count                 # hit counts only (volume check)
    python run_search.py --export OUT_DIR        # write R{n}{x}_{source}.ris + run_manifest.json

arXiv: one request per 3 s (API terms of use). OpenAlex: anonymous, one request per 2.5 s (heavy boolean queries are limited to 1/s).
No personal data is sent (no mailto, no API key).
"""
import argparse, json, os, re, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone

UA = "thesis-literature-search/1.0 (python-urllib)"
YEAR_FROM, YEAR_TO = 2025, 2026

# ---- query blocks (search-plan.md v1.0). Wildcards are expanded into explicit variants,
# because neither API supports truncation reliably.
L = ["large language model", "large language models", "LLM", "LLMs", "language model", "language models",
     "ChatGPT", "GPT-4", "GPT-4o", "chatbot", "chatbots"]

ROUNDS_V10 = {
    "R1a": [L, ["uncertainty quantification", "uncertainty estimation", "confidence estimation",
                "verbalized confidence", "verbalised confidence", "expressed confidence", "calibration",
                "miscalibration", "overconfidence", "overconfident", "semantic entropy", "predictive entropy",
                "self-consistency", "selective prediction", "knowing what they don't know"]],
    "R1b": [L, ["confidence", "uncertainty", "hedging", "epistemic marker", "epistemic markers"],
            ["trust", "reliance", "user perception", "overreliance"]],
    "R2a": [L, ["financial advice", "financial advisor", "financial advisors", "financial adviser",
                "financial advisers", "robo-advisor", "robo-advisors", "robo-adviser", "robo-advisory",
                "investment advice", "investment recommendation", "investment recommendations",
                "personal finance", "financial planning", "retirement planning", "financial literacy"]],
    "R2b": [L, ["finance", "financial", "investment", "investor", "investors"],
            ["uncertainty", "confidence", "calibration", "overconfidence", "overconfident",
             "hallucination", "hallucinations", "consistency"]],
    "R3": [L, ["knowledge acquisition", "fact learning", "factual knowledge", "new knowledge", "new facts",
               "long-tail knowledge", "knowledge memorization", "knowledge memorisation", "fact memorization",
               "knowledge boundary", "knowledge boundaries", "temporal knowledge", "outdated knowledge",
               "knowledge forgetting", "pretraining data frequency"]],
    "R4a": [L, ["epistemic diversity", "knowledge diversity", "whose knowledge", "epistemic", "homogenization",
                "homogenisation", "homogeneity", "knowledge coverage", "cultural knowledge"]],
}

# v1.1 (2026-11-20, volume check): each block is (terms, field); field "ta" = title or abstract,
# "ti" = title only. OpenAlex types limited to article|preprint.
UQ = ["uncertainty quantification", "uncertainty estimation", "confidence estimation", "verbalized confidence",
      "verbalised confidence", "expressed confidence", "confidence calibration", "calibration error",
      "well-calibrated", "miscalibration", "miscalibrated", "overconfidence", "overconfident",
      "semantic entropy", "predictive entropy", "selective prediction", "knowing what they don't know"]
ROUNDS = {
    "R1a": [(L, "ta"), (UQ, "ti")],
    "R1b": [(L, "ta"), (["confidence", "uncertainty", "hedging", "epistemic marker", "epistemic markers"], "ta"),
            (["user trust", "overreliance", "appropriate reliance", "trust calibration", "user perception"], "ta")],
    "R2a": [(L, "ta"), (ROUNDS_V10["R2a"][1], "ta")],
    "R2b": [(L, "ta"), (["finance", "financial", "investment", "investor", "investors"], "ta"),
            (["uncertainty", "confidence", "calibration", "overconfidence", "overconfident",
              "hallucination", "hallucinations"], "ti")],
    "R3": [(L, "ta"), (["knowledge acquisition", "fact learning", "factual knowledge", "learning new knowledge",
                        "new factual knowledge", "new facts", "knowledge injection", "long-tail knowledge",
                        "knowledge memorization", "knowledge memorisation", "fact memorization",
                        "knowledge boundary", "knowledge boundaries", "temporal knowledge", "outdated knowledge",
                        "knowledge forgetting", "pretraining data frequency"], "ti")],
    "R4a": [(L, "ta"), (["epistemic diversity", "knowledge diversity", "whose knowledge", "homogenization",
                         "homogenisation", "knowledge coverage", "cultural knowledge", "epistemic injustice"], "ti")],
}


ROUNDS_V11 = dict(ROUNDS)

# v1.2 (2026-11-20, Frank's choice): LLM term in the TITLE for R1b, R2a, R2b, R4a; R2a also needs an
# uncertainty/consistency/risk term; R1a needs a knowledge or finance term and R3 an uncertainty or finance
# term (option O2, title or abstract); R4b (citation chasing) complete.
FIN = ["finance", "financial", "investment", "investments", "investor", "investors", "stock", "stocks",
       "portfolio", "banking", "bank", "trading", "market", "markets", "economic", "economics", "credit",
       "robo-advisor", "wealth", "fintech"]
KNOW = ["factual", "knowledge", "fact", "facts", "memorization", "memorisation"]
UNCT = ["uncertainty", "uncertain", "confidence", "calibration", "calibrated", "miscalibration", "entropy",
        "hedging", "abstain", "abstention", "I dont know"]
CONC = UNCT + ["consistency", "consistent", "inconsistency", "reliability", "reliable", "hallucination",
               "hallucinations", "risk", "risks"]
ROUNDS = {
    "R1a": ROUNDS_V11["R1a"] + [(KNOW + FIN, "ta")],
    "R1b": [(L, "ti")] + ROUNDS_V11["R1b"][1:],
    "R2a": [(L, "ti")] + ROUNDS_V11["R2a"][1:] + [(CONC, "ta")],
    "R2b": [(L, "ti")] + ROUNDS_V11["R2b"][1:],
    "R3": ROUNDS_V11["R3"] + [(UNCT + FIN, "ta")],
    "R4a": [(L, "ti")] + ROUNDS_V11["R4a"][1:],
}


def get(url, tries=6, pause=5.0):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            if i == tries - 1:
                raise
            print(f"  retry {i+1} after error: {e}", file=sys.stderr)
            time.sleep(pause * (i + 2))


# ---------------------------------------------------------------- arXiv
ATOM = "{http://www.w3.org/2005/Atom}"
OS = "{http://a9.com/-/spec/opensearch/1.1/}"
ARX = "{http://arxiv.org/schemas/atom}"


def arxiv_term(t, field="ta"):
    t = t.replace("'", "")  # arXiv parser chokes on apostrophes
    q = f'"{t}"' if " " in t or "-" in t else t
    return f"ti:{q}" if field == "ti" else f"ti:{q} OR abs:{q}"


def arxiv_query(blocks):
    parts = ["(" + " OR ".join(arxiv_term(t, f) for t in b) + ")" for b, f in blocks]
    date = f"submittedDate:[{YEAR_FROM}01010000 TO {YEAR_TO}12312359]"
    return " AND ".join(parts + [date])


_last = [0.0]


def arxiv_fetch(q, start, n):
    wait = 3.1 - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "start": start, "max_results": n, "sortBy": "submittedDate", "sortOrder": "ascending"})
    body = get(url)
    _last[0] = time.time()
    return ET.fromstring(body)


def arxiv_count(blocks):
    root = arxiv_fetch(arxiv_query(blocks), 0, 1)
    return int(root.findtext(OS + "totalResults") or 0)


def arxiv_records(blocks):
    q = arxiv_query(blocks)
    total = arxiv_count(blocks)
    recs, start, page = [], 0, 500
    while start < total:
        root = arxiv_fetch(q, start, page)
        entries = root.findall(ATOM + "entry")
        if not entries:
            print(f"  arXiv returned an empty page at start={start}; retrying once", file=sys.stderr)
            time.sleep(6)
            root = arxiv_fetch(q, start, page)
            entries = root.findall(ATOM + "entry")
            if not entries:
                break
        for e in entries:
            aid = re.sub(r"v\d+$", "", (e.findtext(ATOM + "id") or "").rsplit("/abs/", 1)[-1])
            recs.append({
                "TY": "RPRT", "TI": " ".join((e.findtext(ATOM + "title") or "").split()),
                "AB": " ".join((e.findtext(ATOM + "summary") or "").split()),
                "AU": [a.findtext(ATOM + "name") for a in e.findall(ATOM + "author")],
                "PY": (e.findtext(ATOM + "published") or "")[:4],
                "DA": (e.findtext(ATOM + "published") or "")[:10],
                "JO": "arXiv", "DO": (e.findtext(ARX + "doi") or ""),
                "UR": f"https://arxiv.org/abs/{aid}", "AN": f"arXiv:{aid}", "DB": "arXiv",
                "M3": "preprint",
            })
        start += len(entries)
        print(f"  arXiv {start}/{total}", file=sys.stderr)
    return recs, total


# ---------------------------------------------------------------- OpenAlex
def oa_term(t):
    return f'"{t}"' if " " in t or "-" in t else t


def oa_filter(blocks):
    parts = []
    for b, f in blocks:
        key = "title.search" if f == "ti" else "title_and_abstract.search"
        parts.append(f"{key}:(" + " OR ".join(oa_term(t.replace("'", "")) for t in b) + ")")
    return ",".join(parts) + f",publication_year:{YEAR_FROM}-{YEAR_TO},type:article|preprint"


def oa_get(params):
    time.sleep(2.5)  # >5 boolean operators: OpenAlex allows 1 heavy search/s without a key
    return json.loads(get("https://api.openalex.org/works?" + urllib.parse.urlencode(params)))


def oa_count(blocks):
    return oa_get({"filter": oa_filter(blocks), "per-page": 1, "select": "id"})["meta"]["count"]


def inv_to_text(inv):
    if not inv:
        return ""
    pos = {}
    for w, idx in inv.items():
        for i in idx:
            pos[i] = w
    return " ".join(pos[i] for i in sorted(pos))


TYMAP = {"article": "JOUR", "preprint": "RPRT", "review": "JOUR", "book-chapter": "CHAP",
         "dissertation": "THES", "editorial": "JOUR", "letter": "JOUR", "other": "GEN"}


def oa_records(blocks):
    sel = ("id,doi,title,publication_year,publication_date,type,type_crossref,authorships,"
           "primary_location,abstract_inverted_index,language")
    # page-based paging: cursor paging needs an API key since 2026 (page paging works to 10,000 results)
    page, recs, total = 1, [], None
    while True:
        d = oa_get({"filter": oa_filter(blocks), "per-page": 200, "page": page, "select": sel})
        total = d["meta"]["count"]
        for w in d["results"]:
            src = ((w.get("primary_location") or {}).get("source") or {})
            recs.append({
                "TY": TYMAP.get(w.get("type"), "GEN"), "TI": " ".join((w.get("title") or "").split()),
                "AB": inv_to_text(w.get("abstract_inverted_index")),
                "AU": [(a.get("author") or {}).get("display_name") or "" for a in w.get("authorships") or []],
                "PY": str(w.get("publication_year") or ""), "DA": w.get("publication_date") or "",
                "JO": src.get("display_name") or "", "DO": (w.get("doi") or "").replace("https://doi.org/", ""),
                "UR": w.get("doi") or w.get("id"), "AN": w.get("id", "").rsplit("/", 1)[-1], "DB": "OpenAlex",
                "M3": f"{w.get('type')}/{w.get('type_crossref')}", "LA": w.get("language") or "",
            })
        page += 1
        print(f"  OpenAlex {len(recs)}/{total}", file=sys.stderr)
        if not d["results"] or len(recs) >= total:
            break
    return recs, total


SEEDS_OA = {"seed1": "W7084854541"}  # Wright et al., What and Whose Knowledge? (arXiv:2510.04226)


def oa_citation_chase(work_id):
    """R4b: backward references + forward citations of a seed, publication_year 2025-2026."""
    time.sleep(2.5)
    w = json.loads(get(f"https://api.openalex.org/works/{work_id}?select=id,referenced_works"))
    refs = [r.rsplit("/", 1)[-1] for r in w.get("referenced_works") or []]
    out = {}
    for label, filt_list in (("backward", ["ids.openalex:" + "|".join(refs[i:i + 50]) for i in range(0, len(refs), 50)]),
                             ("forward", [f"cites:{work_id}"])):
        recs = []
        for flt in filt_list:
            page = 1
            while True:
                sel = ("id,doi,title,publication_year,publication_date,type,type_crossref,authorships,"
                       "primary_location,abstract_inverted_index,language")
                d = oa_get({"filter": f"{flt},publication_year:{YEAR_FROM}-{YEAR_TO}", "per-page": 200,
                            "page": page, "select": sel})
                for x in d["results"]:
                    src = ((x.get("primary_location") or {}).get("source") or {})
                    recs.append({
                        "TY": TYMAP.get(x.get("type"), "GEN"), "TI": " ".join((x.get("title") or "").split()),
                        "AB": inv_to_text(x.get("abstract_inverted_index")),
                        "AU": [(a.get("author") or {}).get("display_name") or "" for a in x.get("authorships") or []],
                        "PY": str(x.get("publication_year") or ""), "DA": x.get("publication_date") or "",
                        "JO": src.get("display_name") or "",
                        "DO": (x.get("doi") or "").replace("https://doi.org/", ""),
                        "UR": x.get("doi") or x.get("id"), "AN": x.get("id", "").rsplit("/", 1)[-1],
                        "DB": f"OpenAlex citation chasing ({label})",
                        "M3": f"{x.get('type')}/{x.get('type_crossref')}", "LA": x.get("language") or "",
                    })
                page += 1
                if len(d["results"]) < 200:
                    break
        out[label] = (recs, len(refs) if label == "backward" else None)
    return out


def write_ris(recs, path):
    with open(path, "w", encoding="utf-8") as f:
        for r in recs:
            f.write(f"TY  - {r['TY']}\n")
            for tag in ("TI", "AB", "PY", "DA", "JO", "DO", "UR", "AN", "DB", "M3", "LA"):
                if r.get(tag):
                    f.write(f"{tag}  - {r[tag]}\n")
            for a in r.get("AU") or []:
                if a:
                    f.write(f"AU  - {a}\n")
            f.write("ER  - \n\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", action="store_true")
    ap.add_argument("--export")
    ap.add_argument("--rounds", default=",".join(ROUNDS))
    ap.add_argument("--sources", default="arxiv,openalex")
    ap.add_argument("--chase", action="store_true", help="R4b citation chasing of SEEDS_OA (needs --export)")
    a = ap.parse_args()
    rounds = a.rounds.split(",")
    manifest = {"run_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "years": [YEAR_FROM, YEAR_TO], "rounds": {}}
    for r in rounds:
        b = ROUNDS[r]
        entry = {"arxiv_query": arxiv_query(b), "openalex_filter": oa_filter(b)}
        if a.count:
            entry["arxiv_hits"] = arxiv_count(b)
            entry["openalex_hits"] = oa_count(b)
            print(f"{r}: arXiv {entry['arxiv_hits']}  OpenAlex {entry['openalex_hits']}", flush=True)
        if a.export:
            for name, fn in (("arxiv", arxiv_records), ("openalex", oa_records)):
                path = f"{a.export}/{r}_{name}.ris"
                if name not in a.sources.split(",") or os.path.exists(path):
                    print(f"{r} {name}: skipped (not selected or already exported: {path})", flush=True)
                    continue
                recs, total = fn(b)
                write_ris(recs, path)
                entry[f"{name}_hits"] = total
                entry[f"{name}_exported"] = len(recs)
                print(f"{r} {name}: {len(recs)}/{total} -> {path}", flush=True)
        manifest["rounds"][r] = entry
    if a.chase and a.export:
        for name, wid in SEEDS_OA.items():
            for label, (recs, nref) in oa_citation_chase(wid).items():
                path = f"{a.export}/R4b_{name}_{label}.ris"
                write_ris(recs, path)
                manifest["rounds"][f"R4b_{name}_{label}"] = {"seed": wid, "exported_2025_2026": len(recs),
                                                             "all_references": nref}
                print(f"R4b {name} {label}: {len(recs)} (2025-2026) -> {path}", flush=True)
    out = a.export + "/run_manifest.json" if a.export else None
    if out:
        old = json.load(open(out)) if os.path.exists(out) else {"runs": []}
        old.setdefault("runs", []).append(manifest)
        with open(out, "w") as f:
            json.dump(old, f, indent=1)
    else:
        print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk.endswith("hits")}
                          for k, v in manifest["rounds"].items()}))


if __name__ == "__main__":
    main()
