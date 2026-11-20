# Screening protocol: full-text stage

Version 1.0, 2026-11-20. Mode: **go light** — single-reviewer full-text check by Claude Opus 5.5 (main session), disclosed in the methods. **Scope (deviation, Frank 2026-11-20):** only the evidence set used for the gaps, RQs and supervisor email (38 records), not all 308 advanced records.

## Eligibility at full text
Same PCC and exclusion codes and order as `screening_protocol.md` v1.0 (E1 year · E2 publication type · E3 not LLMs · E4 finance without concept · E5 concept missing · E9 other). Full-text-only criteria now apply: the report must contain its own empirical analysis or evaluation (position papers with only illustrative examples → E2); reported results must come from observed data (simulated participants presented as findings → E9); concept A/B must be studied, not only mentioned. "Unclear" = information missing from the report. A report that cannot be retrieved is "not retrieved", not excluded.

## Procedure
Text extracted per page (`literature/tools/ft_extract.py`, pypdf); the reviewer reads the opening (abstract/introduction), the section structure, and the discussion/limitations/conclusion, and further pages where eligibility is in doubt. Decisions: `ft_decisions.csv` (id, d, code, why, last_section, page, window, check, attempt, strength).

## Proof of reading (applies to every full-text decision)

- Each decision includes a `last_section` field: a short paraphrase (max 20 words) of something from the report's limitations, discussion or conclusion, with its page marker (e.g. `p. 9`).
- After each batch, every decision is checked. It fails if `last_section` is missing or empty, or if its page marker is not in the last third of the report, counting the pages before the references.
- A failed decision is re-run, at most twice. If it still fails, it is flagged for Frank and not counted (it stays pending; it is never filled in by default).

## Amendment log

| Date | Change | Reason | Records to re-screen |
|------|--------|--------|----------------------|
| 2026-11-20 | Added the proof-of-reading rule above (`last_section` field, last-third page check, max 2 re-runs, then flag for Frank and do not count). | Frank's instruction: evidence that each report was read to the end before a decision counts. | None (full-text stage not started). |
