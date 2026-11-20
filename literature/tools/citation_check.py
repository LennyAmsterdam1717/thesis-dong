#!/usr/bin/env python3
"""Citation check (CLAUDE.md step 3) for the full-text-included evidence set.
Existence: ARS plugin clients (arxiv_client.ArxivClient.arxiv_id_lookup, crossref_client.CrossrefClient
.doi_lookup_with_title_check; both with the 0.70 title cross-check). Metadata (authors, year, venue): arXiv API
and the DOI resolver (doi.org, CSL-JSON content negotiation; covers Crossref and DataCite DOIs).
No personal data sent (no polite email). Raw results -> literature/citation-check/<date>_results.json.
PASS = at least one identifier resolves with matching title, a working link exists, and the year is 2025-2026.
Usage (from literature/): python tools/citation_check.py ids.json   (list of {id, arxiv, doi})"""
import csv, json, os, re, sys, time, urllib.request, difflib
PLUG = os.path.expanduser("~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.24.3/scripts")
sys.path.insert(0, PLUG)
from arxiv_client import ArxivClient          # noqa: E402
from crossref_client import CrossrefClient    # noqa: E402
UA = {"User-Agent": "thesis-citation-check/1.0"}
ATOM = "{http://www.w3.org/2005/Atom}"
import xml.etree.ElementTree as ET

def norm(t): return re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", (t or "").lower())).strip()
def sim(a, b): return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()

def csl(doi):
    req = urllib.request.Request("https://doi.org/" + doi, headers={**UA, "Accept": "application/vnd.citationstyles.csl+json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def arxiv_meta(aid):
    time.sleep(3.1)
    with urllib.request.urlopen(urllib.request.Request(f"http://export.arxiv.org/api/query?id_list={aid}", headers=UA), timeout=60) as r:
        e = ET.fromstring(r.read()).find(ATOM + "entry")
    if e is None: return None
    return dict(title=" ".join((e.findtext(ATOM + "title") or "").split()),
                authors=[a.findtext(ATOM + "name") for a in e.findall(ATOM + "author")],
                published=(e.findtext(ATOM + "published") or "")[:10],
                comment=(e.findtext("{http://arxiv.org/schemas/atom}comment") or ""),
                journal_ref=(e.findtext("{http://arxiv.org/schemas/atom}journal_ref") or ""))

chart = {r["id"]: r for r in csv.DictReader(open("charting.csv", encoding="utf-8-sig"))}
ids = json.load(open(sys.argv[1]))
ax, cr = ArxivClient(), CrossrefClient()
out = []
for e in ids:
    rid = e["id"]; title = chart[rid]["title"]; res = dict(id=rid, record_title=title, record_year=chart[rid]["year"],
                                                           record_first_author=chart[rid]["first_author"], checks=[])
    if e.get("arxiv"):
        try:
            hit = ax.arxiv_id_lookup(e["arxiv"], title)
            m = arxiv_meta(e["arxiv"])
            res["checks"].append(dict(source="arXiv API", id=e["arxiv"], title_match=bool(hit), meta=m,
                                      sim=round(sim(m["title"], title), 3) if m else None))
        except Exception as ex:
            res["checks"].append(dict(source="arXiv API", id=e["arxiv"], error=str(ex)))
    for doi in [d for d in (e.get("doi") or "").split(";") if d and not d.lower().startswith("10.48550/")]:
        c = dict(source="DOI resolver", id=doi)
        try:
            m = csl(doi)
            t = m.get("title") or ""
            if isinstance(t, list): t = t[0] if t else ""
            yr = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
            c.update(title_match=sim(t, title) >= 0.70, sim=round(sim(t, title), 3),
                     meta=dict(title=t, authors=[" ".join(x for x in (a.get("given"), a.get("family")) if x) or a.get("literal", "")
                                                 for a in m.get("author", [])], year=yr, venue=m.get("container-title") or m.get("publisher"),
                               type=m.get("type")))
            try:
                c["crossref_title_check"] = bool(cr.doi_lookup_with_title_check(doi, title))
            except Exception as ex:
                c["crossref_title_check"] = f"n/a ({str(ex)[:60]})"
        except Exception as ex:
            c["error"] = str(ex)[:120]
        res["checks"].append(c)
        time.sleep(1)
    ok = [c for c in res["checks"] if c.get("title_match")]
    years = []
    for c in ok:
        m = c.get("meta") or {}
        years.append(int(m["published"][:4]) if m.get("published") else m.get("year"))
    first_year = min([y for y in years if y]) if years else None
    res["first_public_year"] = first_year
    res["result"] = "PASS" if ok and first_year and 2025 <= int(res["record_year"]) <= 2026 else "FAIL"
    if ok and first_year and first_year < 2025:
        res["note"] = f"earliest version {first_year} (< 2025); record year {res['record_year']} used per protocol"
    out.append(res)
    print(rid, res["result"], [(c["source"], c.get("id"), c.get("sim"), c.get("error", "")[:40]) for c in res["checks"]], res.get("note", ""), flush=True)
os.makedirs("citation-check", exist_ok=True)
json.dump(out, open(f"citation-check/{time.strftime('%Y-%m-%d')}_results.json", "w"), indent=1, ensure_ascii=False)
