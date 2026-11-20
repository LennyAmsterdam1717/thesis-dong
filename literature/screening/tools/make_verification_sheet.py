#!/usr/bin/env python3
"""Draw Frank's post-hoc verification sample: 20 final exclusions + 10 final inclusions (random, seed 2026),
mixed order, with the AI's one-line reason; Frank fills the 'agree_disagree' column (agree / disagree).
Usage (from literature/screening): python tools/make_verification_sheet.py"""
import csv, random
rows = list(csv.DictReader(open("Screening_TA/TA_screening_log_All_Records.csv", encoding="utf-8-sig")))
exc = sorted([r for r in rows if r["Final decision"] == "exclude"], key=lambda r: r["ID"])
inc = sorted([r for r in rows if r["Final decision"] == "include"], key=lambda r: r["ID"])
rng = random.Random(2026)
sample = [("exclude", r) for r in rng.sample(exc, 20)] + [("include", r) for r in rng.sample(inc, 10)]
rng.shuffle(sample)
with open("verification_sheet.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["n", "id", "ai_decision", "ai_code", "ai_reason", "decided_by", "agree_disagree",
                "frank_note", "year", "title", "doi_or_link", "abstract"])
    for n, (_, r) in enumerate(sample, 1):
        link = ("https://doi.org/" + r["DOI"]) if r["DOI"] else ""
        w.writerow([n, r["ID"], r["Final decision"], r["Final code"], r["Final reason"], r["Decided by"], "", "",
                    r["Year"], r["Title"], link, r["Abstract"]])
print(f"exclusions pool {len(exc)}, inclusions pool {len(inc)}; wrote verification_sheet.csv with {len(sample)} rows")
