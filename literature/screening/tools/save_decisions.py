#!/usr/bin/env python3
"""Save one reviewer return (Agent-tool path) as sr_work/decisions/<label with : -> _>.json.
Usage: python tools/save_decisions.py <ROLE> <BATCH> [--index sr_work/prompts_ta_all/index.json] < return.json
ROLE = A | B | ADJ | QC ...; the full label (with @context_id) is taken from index.json, never retyped."""
import json, sys, os, re, argparse
ap = argparse.ArgumentParser(); ap.add_argument("role"); ap.add_argument("batch")
ap.add_argument("--index", default="sr_work/prompts_ta_all/index.json"); ap.add_argument("--work", default="sr_work")
a = ap.parse_args()
idx = json.load(open(a.index))
labels = [e["label"] for e in idx if e["label"].split("@")[0] == f"{a.role}:{a.batch}"]
if len(labels) != 1:
    sys.exit(f"label for {a.role}:{a.batch} not found exactly once in {a.index}: {labels}")
text = sys.stdin.read()
m = re.search(r"\{.*\}", text, re.S)
obj = json.loads(m.group(0))
dec = obj["decisions"] if isinstance(obj, dict) else obj
batch_ids = None
for b in json.load(open(os.path.join(a.work, "manifest.json"))):
    if b["batch"] == a.batch:
        batch_ids = b["ids"]
got = [d["id"] for d in dec]
missing = [i for i in (batch_ids or []) if i not in got]
extra = [i for i in got if batch_ids is not None and i not in batch_ids]
out = os.path.join(a.work, "decisions", labels[0].replace(":", "_") + ".json")
json.dump({"label": labels[0], "decisions": dec}, open(out, "w"), indent=0)
print(f"saved {len(dec)} decisions -> {out}; missing {len(missing)} {missing[:5]}; extra {extra}")
