"""Fetch OpenAlex cited_by_count for every unique record (read-only lookups). Run from literature/screening:
python ../search/fetch_citation_counts.py  -> sr_work/citation_counts.json"""
import json, sys, time, urllib.parse, urllib.request
sys.path.insert(0, "../search"); import run_search as s
ident=json.load(open('sr_work/identification.json')); raw=json.load(open('sr_work/raw_records.json'))
uniq=json.load(open('sr_work/records.json'))['unique']
wid, dois = {}, {}
for u in uniq:
    for i in u['members']:
        r=raw[i]; an=(r.get('AN') or [''])[0]; db=(r.get('DB') or [''])[0]
        if an.startswith('W'): wid[u['id']]=an
        elif an.startswith('arXiv:'): dois.setdefault(u['id'], '10.48550/arxiv.'+an[6:].lower())
    if u['id'] not in wid and u.get('doi'): dois.setdefault(u['id'], u['doi'].lower())
cites={}
def fetch(flt, keyf):
    for i in range(0, len(flt), 50):
        chunk=flt[i:i+50]
        d=s.oa_get({"filter": keyf + "|".join(v for _, v in chunk), "per-page": 50, "select": "id,doi,cited_by_count"})
        bykey={}
        for w in d['results']:
            bykey[w['id'].rsplit('/',1)[-1]]=w['cited_by_count']
            if w.get('doi'): bykey[w['doi'].replace('https://doi.org/','').lower()]=w['cited_by_count']
        for rid, v in chunk:
            if v in bykey: cites[rid]=bykey[v]
fetch([(k,v) for k,v in wid.items()], "ids.openalex:")
fetch([(k,v) for k,v in dois.items() if k not in cites], "doi:")
json.dump({"retrieved_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "cited_by_count": cites}, open('sr_work/citation_counts.json','w'), indent=0)
print(len(uniq), "unique;", len(cites), "with a citation count")
