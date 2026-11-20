#!/usr/bin/env python3
"""Agreement between Frank's verification marks and the AI decisions (verification_sheet.csv).
Usage (from literature/screening): python tools/verification_agreement.py
Prints agree counts overall / for exclusions / for inclusions, lists every disagreement, and
STOPs (exit code 2) if Frank disagrees with any exclusion (Frank's stop rule, 2026-11-20)."""
import csv, sys
rows = list(csv.DictReader(open("verification_sheet.csv", encoding="utf-8-sig")))
marks = {r["id"]: r["agree_disagree"].strip().lower() for r in rows}
blank = [r["id"] for r in rows if marks[r["id"]] not in ("agree", "disagree")]
if blank:
    sys.exit(f"not finished: {len(blank)} rows without agree/disagree: {blank}")
def tally(kind):
    sub = [r for r in rows if r["ai_decision"] == kind]
    return sum(marks[r["id"]] == "agree" for r in sub), len(sub)
ea, en = tally("exclude"); ia, inn = tally("include")
print(f"overall {ea + ia}/{en + inn} agree ({(ea + ia) / (en + inn):.0%}); exclusions {ea}/{en}; inclusions {ia}/{inn}")
dis = [r for r in rows if marks[r["id"]] == "disagree"]
for r in dis:
    print(f"  disagree: {r['id']} AI={r['ai_decision']} {r['ai_code']} | {r['title'][:80]} | note: {r['frank_note']}")
if any(r["ai_decision"] == "exclude" for r in dis):
    print("STOP: Frank disagrees with at least one exclusion -> do not start full text; review exclusion rules first.")
    sys.exit(2)
