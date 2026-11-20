# Screening (SR-Screener)

Holds `screening_protocol.md` (v1.0, confirmed 2026-11-20), `screening_config.json`, `ft_protocol.md` (stub + amendment log), `inputs/` (v1.2 search exports + `run_manifest.json`), `sr_work/` (records, batches, identification counts, `pilot_sample.json`), `pilot_labels.csv`, `tools/make_pilot_batch.py`, `archive/` (v1.1 exports and work folder, not used for screening); later `overrides.csv`, `Screening_TA/`, `Screening_FT/`.

PDFs go in `fulltext/` (git-ignored); extracted text in `fulltext_txt/` (git-ignored).

## Status (2026-11-20)

- 669 unique records (search v1.2) in 15 batches. **b001 = mixed pilot batch of 25 records** across all rounds, including the seed (R00559).
- **Frank: label the pilot.** Read `sr_work/batches/b001.txt` and fill in `pilot_labels.csv` **without looking at any AI output**: `d` = `include` / `unclear` / `exclude`; `code` = `INC`, `UNC` or the first failing exclusion code from the protocol (E1–E5, E9); `why` = a few words; `by` = Frank.
- No AI screening has been run yet.
