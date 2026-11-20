#!/usr/bin/env python3
"""Full-text helper (go-light single-reviewer check). For each PDF in screening/fulltext/:
page count, first page of the reference list, the 'last third' window (pages before the references),
section headings, opening text, and Discussion/Limitations/Conclusion text with page markers.
Writes screening/fulltext_txt/<ID>.json (git-ignored) and prints a compact digest.
Usage: python ft_extract.py ID [ID ...]   (needs pypdf)"""
import json, re, sys, os
from pypdf import PdfReader
BASE = os.path.join(os.path.dirname(__file__), "..", "screening")
os.makedirs(os.path.join(BASE, "fulltext_txt"), exist_ok=True)
HEAD = re.compile(r"^\s*(?:\d+(?:\.\d+)*\.?\s+|[IVX]+\.\s+)?(Introduction|Related Work|Background|Method(?:s|ology)?|Approach|Experiments?|Experimental Setup|Results?|Analysis|Discussion|Limitations?|Conclusions?|Conclusion and Future Work|Future Work|Ethics|Broader Impact)\b", re.I | re.M)
END = re.compile(r"^\s*(?:\d+\.?\s*)?(Discussion|Limitations?|Conclusions?|Concluding Remarks|Future Work)\b", re.I | re.M)
for rid in sys.argv[1:]:
    pages = [(p.extract_text() or "") for p in PdfReader(os.path.join(BASE, "fulltext", rid + ".pdf")).pages]
    n = len(pages)
    ref = next((i + 1 for i, t in enumerate(pages) if i > 1 and re.search(r"^\s*(References|Bibliography|REFERENCES)\s*$", t, re.M)), n)
    body = ref  # pages 1..ref count as the report body (ref page may hold the end of the conclusion)
    last_third_from = int(body - body / 3) + 1
    heads = []
    for i, t in enumerate(pages[:ref]):
        for m in HEAD.finditer(t):
            heads.append(f"p{i+1}:{m.group(0).strip()[:40]}")
    endtxt = []
    for i in range(ref - 1, max(-1, ref - 6), -1):
        t = pages[i]
        m = END.search(t)
        if m:
            endtxt.append((i + 1, re.sub(r"\s+", " ", t[m.start():])[:1400]))
    endtxt.sort()
    d = dict(id=rid, pages=n, references_page=ref, last_third_from_page=last_third_from,
             headings=heads[:25], opening=re.sub(r"\s+", " ", " ".join(pages[:2]))[:1500], end_sections=endtxt[-3:])
    json.dump(d, open(os.path.join(BASE, "fulltext_txt", rid + ".json"), "w"), indent=1)
    print(f"=== {rid}: {n} pages, references p{ref}, last third = p{last_third_from}-p{ref}")
    print("headings:", " | ".join(heads[:18]))
    print("opening:", d["opening"][:700])
    for p, t in endtxt[-2:]:
        print(f"[p{p}] {t[:900]}")
    print()
