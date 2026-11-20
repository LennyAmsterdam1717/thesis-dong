# Screening (SR-Screener)

Holds `screening_protocol.md` (v1.0, confirmed 2026-11-20), `screening_config.json`, `ft_protocol.md` (stub + amendment log), `inputs/` (v1.2 search exports + `run_manifest.json`), `sr_work/` (records, batches, identification counts, `pilot_sample.json`), `pilot_labels.csv`, `tools/make_pilot_batch.py`, `archive/` (v1.1 exports and work folder, not used for screening); later `overrides.csv`, `Screening_TA/`, `Screening_FT/`.

PDFs go in `fulltext/` (git-ignored); extracted text in `fulltext_txt/` (git-ignored).

## Status (2026-11-20)

- Title/abstract screening complete (no human pilot; recorded override). After 15 overrides — **2 by Frank, 13 AI judgments by Claude** although SR-Screener labels all 15 "human" (see `Screening_TA/NOTE_overrides_and_verification.md`) — 308 advance (197 include, 111 unclear), 361 excluded.
- Verification sample (`verification_sheet.csv`) checked by Claude on Frank's behalf (28/30 agree); no human verification.
- Full text: targeted single-reviewer check of the evidence set only (`ft_protocol.md`, `ft_decisions.csv`): 30 + 3 (other methods) included; 6 not retrieved (R00203, R00333, R00340, R00475, R00530, OM3).
