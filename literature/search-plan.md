# Search plan R1–R4 (v1.0, confirmed by Frank 2026-11-20)

_Drafted 2026-11-20. Nothing has been searched yet. Once confirmed, each executed round goes into `search-log.md` with date, exact string, filters, hits and PRISMA 2020 counts._

## Common settings

- **Years:** 2025–2026 (filter applied in every source; E1 in the protocol catches leftovers).
- **Language:** English (others flagged, not excluded).
- **Sources:**
  - **arXiv API** (title + abstract; all categories): preprints. Follows ARS `deep-research/references/arxiv_api_protocol.md`.
  - **OpenAlex API** (`title_and_abstract.search`, `publication_year:2025-2026`, types article / preprint / proceedings): covers journals and proceedings (incl. most of the ACL Anthology). Follows `openalex_api_protocol.md`. Free, no institutional access needed.
  - _Optional, not used for now:_ **Scopus** via UU (Frank exports RIS by hand).
- **Export format:** one CSV/RIS file per round and source in `literature/screening/inputs/` (e.g. `R1_arxiv.csv`, `R1_openalex.ris`), with title, abstract, authors, year, venue, DOI/arXiv ID, so `prepare_records.py` can parse them.
- **Screening:** all R1–R4 exports are de-duplicated together and screened as one set (one pilot, one full run); PRISMA identification counts are still reported per round and source.
- **Volume check:** hit counts are recorded first. If the de-duplicated total exceeds ~2,500 records, Claude proposes tighter strings to Frank before exporting (screening cost scales with records: ~50 records per batch × 2 reviewers).

LLM block used in every round:
`L = ("large language model*" OR LLM OR LLMs OR "language model*" OR ChatGPT OR "GPT-4*" OR chatbot*)`

## R1 – Uncertainty quantification and calibration (direction A; directions 1, 2, 4)

R1a: `L AND ("uncertainty quantification" OR "uncertainty estimation" OR "confidence estimation" OR "verbalized confidence" OR "verbalised confidence" OR "expressed confidence" OR calibration OR miscalibration OR overconfiden* OR "semantic entropy" OR "predictive entropy" OR "self-consistency" OR "selective prediction" OR "knowing what they don't know")`

R1b (user perception of confidence): `L AND (confidence OR uncertainty OR hedging OR "epistemic marker*") AND (trust OR reliance OR "user perception" OR overreliance)`

## R2 – LLMs and financial advice (directions 3, 7)

R2a: `L AND ("financial advice" OR "financial advisor*" OR "financial adviser*" OR "robo-advis*" OR "investment advice" OR "investment recommendation*" OR "personal finance" OR "financial planning" OR "retirement planning" OR "financial literacy")`

R2b: `L AND (finance OR financial OR investment OR investor*) AND (uncertainty OR confidence OR calibration OR overconfiden* OR hallucinat* OR consistency)`

Many R2a hits will be E4 (finance without concept) and go to `background.md`; that is intended.

## R3 – Knowledge acquisition and fact learning (direction B; direction 5)

`L AND ("knowledge acquisition" OR "fact learning" OR "factual knowledge" OR "new knowledge" OR "new facts" OR "long-tail knowledge" OR "knowledge memorization" OR "knowledge memorisation" OR "fact memorization" OR "knowledge boundar*" OR "temporal knowledge" OR "outdated knowledge" OR "knowledge forgetting" OR "pretraining data frequency")`

## R4 – Epistemic diversity / knowledge representation + citation chasing (direction 6)

R4a (database): `L AND ("epistemic diversity" OR "knowledge diversity" OR "whose knowledge" OR "epistemic" OR homogeni* OR "knowledge coverage" OR "cultural knowledge")`

R4b (citation chasing, PRISMA "other methods"): backward references and forward citations of seed 1 (Wright et al., 2026, EMNLP) via OpenAlex / Semantic Scholar, filtered to 2025–2026. Repeated for seed 2 if one is added.

## R5 – Google Scholar cross-check (later, runbook step 8)

Not part of this draft: run after the gap analysis to test "nobody has done X" claims; missed papers enter through the "other methods" branch.
