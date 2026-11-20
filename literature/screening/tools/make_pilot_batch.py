#!/usr/bin/env python3
"""Re-batch sr_work so that b001 is ONE mixed pilot batch of N records sampled across all search rounds.

Why: prepare_records.py batches records in export order, so its b001 holds records from one round only.
Frank (2026-11-20) asked for a single mixed pilot batch of 25 records across all rounds, incl. the seed.

What it does (before any build_workflow.py call, so review_state.json binds the final batches):
- reads sr_work/records.json, raw_records.json, identification.json (round = export file prefix);
- stratified random sample (fixed seed): the seed record(s) from screening_config.json are always in;
  the other slots are split over rounds in proportion to their unique records (min 2 per round),
  each record counted under its first round in R1a, R1b, R2a, R2b, R3, R4a, R4b order;
- b001 = the sample (in ID order); the rest re-batched in ID order with the config's max_records/max_chars;
- batch files are written with srlib.record_block (the same text prepare_records.py writes);
- record IDs do not change; records.json 'batch' fields, manifest.json and identification.json 'batches'
  are updated; sr_work/pilot_sample.json records the sample, its strata and the random seed.

Usage (from literature/screening):
  python tools/make_pilot_batch.py --work sr_work --config screening_config.json --n 25 --seed 2026
"""
import argparse, glob, json, os, random, sys

SR = os.path.expanduser("~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.24.3/sr-screener/scripts")
sys.path.insert(0, SR)
import srlib  # noqa: E402

ORDER = ["R1a", "R1b", "R2a", "R2b", "R3", "R4a", "R4b"]

ap = argparse.ArgumentParser()
ap.add_argument("--work", required=True)
ap.add_argument("--config", required=True)
ap.add_argument("--n", type=int, default=25)
ap.add_argument("--seed", type=int, default=2026)
a = ap.parse_args()

cfg = srlib.load_config(a.config)
W = a.work
recs = srlib.load_json(os.path.join(W, "records.json"))
uniq = recs["unique"]
ident = srlib.load_json(os.path.join(W, "identification.json"))
if os.path.exists(os.path.join(W, "review_state.json")) or os.path.exists(os.path.join(W, "pilot_batches.json")):
    sys.exit("STOP: screening state already exists; re-batching now would invalidate it.")

fileof = []
for f in ident["files"]:
    fileof += [f["file"].split("_")[0]] * f["records"]
for u in uniq:
    rounds = {fileof[i] for i in u["members"]}
    u_round = next(r for r in ORDER if r in rounds)
    u["_round"] = u_round

seeds = srlib.load_json(os.path.join(W, "seeds.json"), [])
seed_ids = [s["id"] for s in seeds if s.get("id")]
by_round = {r: [u["id"] for u in uniq if u["_round"] == r and u["id"] not in seed_ids] for r in ORDER}
slots = a.n - len(seed_ids)
total = sum(len(v) for v in by_round.values())
alloc = {r: max(2, round(slots * len(v) / total)) for r, v in by_round.items() if v}
while sum(alloc.values()) > slots:          # trim the largest strata first
    r = max(alloc, key=lambda k: (alloc[k], len(by_round[k])))
    alloc[r] -= 1
while sum(alloc.values()) < slots:
    r = max(alloc, key=lambda k: len(by_round[k]) / alloc[k])
    alloc[r] += 1

rng = random.Random(a.seed)
sample = list(seed_ids)
for r in ORDER:
    if r in alloc:
        sample += rng.sample(sorted(by_round[r]), alloc[r])
sample_set = set(sample)

byid = {u["id"]: u for u in uniq}
bcfg = cfg["batching"]
batches = [[byid[i] for i in sorted(sample_set)]]
cur, size = [], 0
for u in uniq:
    if u["id"] in sample_set:
        continue
    block = srlib.record_block(u, bcfg["wrap"])
    if cur and (size + len(block) > bcfg["max_chars"] or len(cur) >= bcfg["max_records"]):
        batches.append(cur)
        cur, size = [], 0
    cur.append(u)
    size += len(block)
if cur:
    batches.append(cur)

bdir = os.path.join(W, "batches")
for f in glob.glob(os.path.join(bdir, "b*.txt")):
    os.remove(f)
manifest, max_lines = [], 0
bw = max(3, len(str(len(batches))))
for bi, b in enumerate(batches, 1):
    name = "b" + str(bi).zfill(bw)
    path = os.path.join(bdir, name + ".txt")
    ids = [u["id"] for u in b]
    blocks = [srlib.record_block(u, bcfg["wrap"]) for u in b]
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(f"BATCH {name} -- {len(ids)} records: {ids[0]} .. {ids[-1]}\n\n")
        f.write("\n".join(blocks))
        f.write(f"\n=== END OF BATCH {name} ({len(ids)} records) ===\n")
    for u, t in zip(b, blocks):
        u["batch"] = name
        max_lines = max(max_lines, t.count("\n") + 1)
    manifest.append(dict(batch=name, path=path.replace("\\", "/"), ids=ids))

strata = {u_id: byid[u_id]["_round"] for u_id in sorted(sample_set)}
for u in uniq:
    u.pop("_round", None)
srlib.save_json(os.path.join(W, "manifest.json"), manifest)
srlib.save_json(os.path.join(W, "records.json"), recs)
ident["batches"] = len(manifest)
ident["max_record_lines"] = max_lines
ident["rebatched_by"] = "tools/make_pilot_batch.py (b001 = stratified mixed pilot sample)"
srlib.save_json(os.path.join(W, "identification.json"), ident, indent=1)
srlib.save_json(os.path.join(W, "pilot_sample.json"),
                dict(n=len(sample_set), random_seed=a.seed, seed_records=seed_ids, allocation=alloc,
                     round_population={r: len(v) for r, v in by_round.items()}, records=strata), indent=1)
print(f"b001: {len(sample_set)} records; allocation {alloc} + seed {seed_ids}; total batches {len(manifest)}")
