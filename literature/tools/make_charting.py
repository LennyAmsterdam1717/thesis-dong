#!/usr/bin/env python3
"""Chart all records advanced at title/abstract (include + unclear) into literature/charting.csv.
Keyword-assisted charting from title + abstract ONLY (no full text): every coded column is a rule-based
tag that a human/Claude refines later; 'ta_reason' is the screening reviewers' one-line reason.
Usage (from literature/): python tools/make_charting.py"""
import csv, json, re
S = "screening/"
rows = list(csv.DictReader(open(S + "Screening_TA/TA_screening_log_All_Records.csv", encoding="utf-8-sig")))
ident = json.load(open(S + "sr_work/identification.json"))
uniq = {u["id"]: u for u in json.load(open(S + "sr_work/records.json"))["unique"]}
raw = json.load(open(S + "sr_work/raw_records.json"))
fileof = []
for f in ident["files"]:
    fileof += [f["file"].split("_")[0]] * f["records"]

def rx(*p): return re.compile("|".join(p), re.I)
DIR = {  # research directions (README / decisions.md working list)
    "1 UQ methods": rx(r"uncertainty (quantif|estimat)", r"semantic entropy", r"predictive entropy", r"token[- ]level uncert",
                       r"conformal", r"sampling[- ]based", r"self[- ]consisten", r"\bprobe", r"hidden[- ]state", r"logit",
                       r"claim[- ]level", r"hallucination detect"),
    "2 calibration/overconfidence": rx(r"calibrat", r"overconfiden", r"over-confiden", r"verbali[sz]ed confidence",
                                        r"expressed confidence", r"stated confidence", r"selective prediction", r"abstain|abstention|refus"),
    "3 finance advice": rx(r"financ", r"invest", r"stock", r"portfolio", r"robo-advis", r"banking", r"trading", r"tax\b",
                           r"accounting", r"credit", r"retirement", r"wealth", r"insurance", r"monetary", r"market"),
    "4 user perception/trust": rx(r"user trust", r"\btrust", r"relian", r"user (study|perception)", r"participants",
                                  r"human perception", r"hedg", r"epistemic marker"),
    "5 knowledge acquisition": rx(r"knowledge acquisition", r"fact(ual)? learning", r"new (facts|knowledge)", r"fine-tun\w* .{0,40}(knowledge|facts)",
                                  r"pre-?train\w* .{0,40}(knowledge|facts|frequency)", r"memori[sz]", r"long[- ]tail", r"knowledge injection",
                                  r"forget", r"outdated", r"temporal knowledge", r"knowledge boundar"),
    "6 epistemic diversity / whose knowledge": rx(r"epistemic diversity", r"whose knowledge", r"cultural knowledge", r"homogen",
                                                  r"knowledge diversity", r"knowledge collapse", r"knowledge coverage", r"culture"),
    "7 datasets/benchmarks": rx(r"\bbenchmark", r"\bdataset", r"\bcorpus"),
}
CONCEPT_A = rx(r"uncertaint", r"confiden", r"calibrat", r"entropy", r"hedg", r"abstain|abstention", r"knowledge boundar")
CONCEPT_B = rx(r"knowledge", r"\bfacts?\b", r"factual", r"memori[sz]", r"epistemic", r"cultur")
FIN = DIR["3 finance advice"]
TYPE = [("survey/review", rx(r"\bsurvey\b", r"\breview\b")),
        ("user study", rx(r"participants", r"user study", r"experiment with \d+", r"survey of \d+", r"between-subjects", r"n ?= ?\d+")),
        ("benchmark/dataset", rx(r"we (introduce|present|release|construct) .{0,60}(benchmark|dataset)", r"\bbenchmark\b")),
        ("method", rx(r"we propose", r"we introduce", r"novel (method|framework|approach)", r"our method", r"framework")),
        ("empirical analysis", rx(r"we (find|show|analy[sz]e|study|investigate|evaluate|examine)", r"systematic evaluation", r"analysis"))]
MODELS = rx(r"GPT-?[345](\.\d)?o?(-mini)?", r"ChatGPT", r"Llama[- ]?\d?(\.\d)?", r"Qwen\d?(\.\d)?", r"Mistral", r"Gemini", r"Claude",
            r"DeepSeek(-R1|-V3)?", r"Gemma", r"Phi-\d", r"OLMo", r"Pythia", r"Falcon", r"Bard")

out = []
for r in rows:
    if r["Final decision"] not in ("include", "unclear"):
        continue
    t = r["Title"] + " " + r["Abstract"]
    u = uniq[r["ID"]]
    rounds = sorted({fileof[i] for i in u["members"]})
    dirs = [k for k, p in DIR.items() if p.search(t)]
    ca, cb = bool(CONCEPT_A.search(t)), bool(CONCEPT_B.search(t))
    stype = next((name for name, p in TYPE if p.search(t)), "unclear from abstract")
    models = sorted({m.group(0) for m in MODELS.finditer(t)})
    src = r["Sources"]
    peer = "preprint" if ("arXiv" in src and not r["DOI"]) or "preprint" in r["Publication type"].lower() else "venue/other"
    link = ("https://doi.org/" + r["DOI"]) if r["DOI"] else ""
    if not link:
        link = next((raw[i]["UR"][0] for i in u["members"] if raw[i].get("UR")), "")
    out.append({
        "id": r["ID"], "ta_decision": r["Final decision"], "decided_by": r["Decided by"], "year": r["Year"],
        "first_author": r["First author"], "title": r["Title"], "venue": r["Journal"], "preprint_or_venue": peer,
        "doi_or_url": link, "search_rounds": "+".join(rounds),
        "directions_kw": "; ".join(dirs), "concept_kw": "+".join(x for x, f in (("A", ca), ("B", cb)) if f) or "-",
        "finance_kw": "yes" if FIN.search(t) else "no", "study_type_kw": stype, "models_named": "; ".join(models),
        "has_abstract": "yes" if r["Abstract"].strip() else "no", "ta_reason": r["Final reason"],
        "evidence_set": "", "fulltext_checked": "", "notes": "", "abstract": r["Abstract"],
    })
out.sort(key=lambda d: d["id"])
with open("charting.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader(); w.writerows(out)
print(len(out), "records charted -> literature/charting.csv")
