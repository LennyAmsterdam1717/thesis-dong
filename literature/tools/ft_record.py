#!/usr/bin/env python3
"""Append/replace full-text decisions in screening/ft_decisions.csv and run the proof-of-reading check
(Frank's rule, ft_protocol.md): last_section present (<= 20 words) and its page marker inside the last third
of the report before the references (window from fulltext_txt/<ID>.json). Failing rows get check=FAIL.
Usage: python ft_record.py decisions.json   (list of {id,d,code,why,last_section,page,strength})"""
import csv, json, os, sys
B = os.path.join(os.path.dirname(__file__), "..", "screening")
P = os.path.join(B, "ft_decisions.csv")
F = ["id", "d", "code", "why", "last_section", "page", "window", "check", "attempt", "strength", "reviewer"]
rows = {r["id"]: r for r in csv.DictReader(open(P, encoding="utf-8"))} if os.path.exists(P) else {}
for d in json.load(open(sys.argv[1])):
    meta = json.load(open(os.path.join(B, "fulltext_txt", d["id"] + ".json")))
    lo, hi = meta["last_third_from_page"], meta["references_page"]
    ls = (d.get("last_section") or "").strip()
    ok = bool(ls) and len(ls.split()) <= 20 and str(d.get("page", "")).isdigit() and lo <= int(d["page"]) <= hi
    prev = rows.get(d["id"])
    rows[d["id"]] = dict(id=d["id"], d=d["d"], code=d["code"], why=d["why"], last_section=ls, page=d.get("page", ""),
                         window=f"p{lo}-p{hi}", check="PASS" if ok else "FAIL",
                         attempt=str(int(prev["attempt"]) + 1) if prev else "1", strength=d.get("strength", ""),
                         reviewer="Claude Opus 5.5 (single reviewer, go light)")
    print(d["id"], rows[d["id"]]["check"], rows[d["id"]]["window"], "page", d.get("page"), len(ls.split()), "words")
with open(P, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=F); w.writeheader(); w.writerows(rows[k] for k in sorted(rows))
