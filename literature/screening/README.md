# Screening (SR-Screener)

Holds `screening_protocol.md` (v1.0, confirmed 2026-11-20), `screening_config.json`, `ft_protocol.md` (stub + amendment log), `inputs/` (v1.2 search exports + `run_manifest.json`), `sr_work/` (records, batches, identification counts, `pilot_sample.json`), `pilot_labels.csv`, `tools/make_pilot_batch.py`, `archive/` (v1.1 exports and work folder, not used for screening); later `overrides.csv`, `Screening_TA/`, `Screening_FT/`.

PDFs go in `fulltext/` (git-ignored); extracted text in `fulltext_txt/` (git-ignored).

## Status (2026-11-20)

- Title/abstract screening **complete** (no human pilot — recorded override; see `docs/decisions.md`): 669 records → 293 advance (197 include, 96 unclear), 376 excluded. A/B agreement 97.0 %, κ 0.939. Outputs in `Screening_TA/`.
- **Frank: fill in `verification_sheet.csv`** — 30 rows (20 exclusions, 10 inclusions, mixed). Put `agree` or `disagree` in the `agree_disagree` column (optional note in `frank_note`). Then run `python tools/verification_agreement.py` (or ask Claude). If you disagree with any exclusion, the work stops before full text.
- `pilot_labels.csv` is unused (pilot skipped).
