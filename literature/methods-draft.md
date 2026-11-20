# Methods draft – literature selection

_To be written after screening. Will cover: review form (integrative review used for a scoping purpose, ARS `lit-review` mode), year range, sources, eligibility (PCC), search rounds and strings, de-duplication, calibration pilot, dual AI title/abstract screening with adjudication and QC recheck, full-text method (dual or single reviewer, as chosen), citation check, PRISMA 2020 counts, and Frank's human verification of the included set._

## Notes for the full-text methods text (to include)

- Full text (go light): single-reviewer check by Claude, disclosed as such.
- Proof of reading: every full-text decision had to include a paraphrase (≤ 20 words) of a point from the limitations, discussion or conclusion with its page marker, located in the last third of the report (before the references); decisions failing this check were re-run up to twice, and any that still failed were flagged for Frank and not counted. Report how many decisions were re-run and how many were flagged.
- Search: v1.0 strings exceeded the volume ceiling and were tightened to v1.1 (concept terms in the title for R1a, R2b, R3, R4a); state the sensitivity trade-off and the mitigations (citation chasing, Google Scholar cross-check).

- Corpus size: v1.1 gave 1,854 unique records, too many for the review's purpose (2–3 RQs). Frank chose to narrow it (v1.2): an LLM term was required in the title for R1b, R2a, R2b and R4a; R2a also had to mention uncertainty, consistency or risk; R1a records had to mention knowledge or finance and R3 records uncertainty or finance; citation chasing (R4b) stayed complete. The v1.2 search found 788 database records and 65 records by citation chasing; after removing 184 duplicates, 669 records were screened. State the trade-off: title-level and cross-concept filters favour precision over sensitivity, so the corpus is a focused sample centred on the links between LLM certainty, knowledge and finance, not a complete map of each field; general methods papers are covered as background. The seed paper was retrieved by the search itself.
- **Deviation – no human calibration pilot.** The review author decided not to label a calibration pilot. Title/abstract screening was started without a passing human-labelled pilot, using SR-Screener's recorded pilot override (reason recorded in `sr_work/pilot_override.json`). Instead, a post-hoc verification sample was checked by the author: 20 randomly drawn exclusions and 10 randomly drawn inclusions, each with the AI's one-line reason, marked agree/disagree. Agreement: [TO COMPLETE: n agree / 30; exclusions x/20; inclusions y/10]. (The first batch had been formed as a stratified mixed sample of 25 records for the planned pilot; it was screened as a normal batch.)

## Disclosure of AI use

_To be completed: which models (with version) did what (search, screening reviewers A/B, adjudicator, QC, full-text check, citation check, drafting), which decisions were made by Frank, and that Frank verified the included set and can explain all AI-produced output._
