# Screening (SR-Screener)

Holds `screening_protocol.md` (v1.0, confirmed 2026-11-20), `screening_config.json`, `ft_protocol.md` (stub + amendment log), `inputs/` (search exports + `run_manifest.json`), `sr_work/` (records, batches, identification counts), `pilot_labels.csv`; later `overrides.csv`, `Screening_TA/`, `Screening_FT/`.

PDFs go in `fulltext/` (git-ignored); extracted text in `fulltext_txt/` (git-ignored).

## Status (2026-11-20)

- 1,854 unique records in 43 batches (`sr_work/batches/b001.txt` … `b043.txt`).
- **Frank: label the pilot.** Read `sr_work/batches/b001.txt` (records R00001–R00050) and fill in `pilot_labels.csv` **without looking at any AI output**: `d` = `include` / `unclear` / `exclude`; `code` = `INC`, `UNC` or the first failing exclusion code from the protocol (E1–E5, E9); `why` = a few words; `by` = Frank.
- No AI screening has been run yet (not on b001, not on any batch).
