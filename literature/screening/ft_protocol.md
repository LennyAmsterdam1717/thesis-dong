# Screening protocol: full-text stage

_Stub, 2026-11-20. The full protocol text is written in runbook step 4 (copy of `screening_protocol.md` v1.0 adapted to full text, per the sr-screener template). Mode: **go light** — single-reviewer full-text check by Claude, disclosed in the methods._

## Proof of reading (applies to every full-text decision)

- Each decision includes a `last_section` field: a short paraphrase (max 20 words) of something from the report's limitations, discussion or conclusion, with its page marker (e.g. `p. 9`).
- After each batch, every decision is checked. It fails if `last_section` is missing or empty, or if its page marker is not in the last third of the report, counting the pages before the references.
- A failed decision is re-run, at most twice. If it still fails, it is flagged for Frank and not counted (it stays pending; it is never filled in by default).

## Amendment log

| Date | Change | Reason | Records to re-screen |
|------|--------|--------|----------------------|
| 2026-11-20 | Added the proof-of-reading rule above (`last_section` field, last-third page check, max 2 re-runs, then flag for Frank and do not count). | Frank's instruction: evidence that each report was read to the end before a decision counts. | None (full-text stage not started). |
