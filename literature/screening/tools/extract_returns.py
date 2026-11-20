#!/usr/bin/env python3
"""Agent-tool path: take each reviewer subagent's final hand-back (its JSON decisions) from the subagent
transcript and save it via save_decisions.py, so returns are never retyped by hand.
Usage (from literature/screening): python tools/extract_returns.py TASKS_DIR ROLE:BATCH=AGENTFILE ... [--index ...]"""
import json, os, subprocess, sys
args = [a for a in sys.argv[1:] if not a.startswith("--index")]
idx = [a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--index=")]
tasks = args[0]
for spec in args[1:]:
    rb, agent = spec.split("=")
    role, batch = rb.split(":")
    msg = None
    for line in open(os.path.join(tasks, agent + ".output")):
        o = json.loads(line)
        c = (o.get("message") or {}).get("content")
        if isinstance(c, list):
            for x in c:
                if x.get("type") == "tool_use" and x.get("name") == "SubagentHandback":
                    msg = x["input"]["message"]
    if msg is None:
        print(f"{rb}: no hand-back found"); continue
    cmd = [sys.executable, "-I", os.path.join(os.path.dirname(__file__), "save_decisions.py"), role, batch]
    if idx: cmd += ["--index", idx[0]]
    r = subprocess.run(cmd, input=msg, text=True, capture_output=True)
    print(rb, (r.stdout or r.stderr).strip())
