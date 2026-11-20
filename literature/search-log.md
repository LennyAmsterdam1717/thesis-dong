# Search log

One entry per search round: date, source, query string, filters, hits, and PRISMA 2020 counts (identified → duplicates removed → screened → excluded → full text sought → not retrieved → assessed → included).

Script: `literature/search/run_search.py` (stdlib only; exact queries sent are stored in `literature/screening/inputs/run_manifest.json`). Exports: `literature/screening/inputs/*.ris`.

## 2026-11-20 – Volume check: v1.0 strings too broad → tightened to v1.1

Plan v1.0 (`search-plan.md`) set a ceiling of ~2,500 records after de-duplication. v1.0 hit counts (2025–2026, title + abstract, OpenAlex all types) were far above it, so Claude tightened the strings (Frank's instruction of 2026-11-20: tighten without his input, keep 2025–2026, keep both sources, keep all 7 directions).

**v1.0 strings:** as in `search-plan.md` § R1–R4 (all blocks searched in title or abstract; OpenAlex types article, preprint, review, book-chapter, dissertation, editorial, letter, other).

**Change 1 – narrower terms + OpenAlex type filter** (still title or abstract):
- R1a: `calibration` → `"confidence calibration" OR "calibration error" OR well-calibrated OR miscalibrated` (+ miscalibration kept); `self-consistency` dropped (mostly a reasoning technique, not a confidence measure).
- R1b: 3rd block `trust OR reliance OR "user perception" OR overreliance` → `"user trust" OR overreliance OR "appropriate reliance" OR "trust calibration" OR "user perception"`.
- R2b: `consistency` dropped from the concept block.
- R3: `"new knowledge"` → `"learning new knowledge" OR "new factual knowledge"`; `"knowledge injection"` added.
- R4a: bare `epistemic` and `homogeneity` dropped; `"epistemic injustice"` added.
- OpenAlex: types limited to `article|preprint` (other types are E2 anyway).

**Change 2 – concept terms required in the title** for R1a, R2b (concept block only), R3, R4a. The LLM block (and R2b's finance block) stay title-or-abstract. R1b and R2a stay fully title-or-abstract (small rounds; finance is the priority context).

**v1.1 final strings** (`L` = `"large language model(s)" OR LLM OR LLMs OR "language model(s)" OR ChatGPT OR GPT-4 OR GPT-4o OR chatbot(s)`, title or abstract; `[ti]` = title only; years 2025–2026):
- R1a: `L AND [ti]("uncertainty quantification" OR "uncertainty estimation" OR "confidence estimation" OR "verbalized confidence" OR "verbalised confidence" OR "expressed confidence" OR "confidence calibration" OR "calibration error" OR "well-calibrated" OR miscalibration OR miscalibrated OR overconfidence OR overconfident OR "semantic entropy" OR "predictive entropy" OR "selective prediction" OR "knowing what they dont know")`
- R1b: `L AND (confidence OR uncertainty OR hedging OR "epistemic marker(s)") AND ("user trust" OR overreliance OR "appropriate reliance" OR "trust calibration" OR "user perception")`
- R2a: `L AND ("financial advice" OR "financial advisor(s)" OR "financial adviser(s)" OR "robo-advisor(s)" OR "robo-adviser" OR "robo-advisory" OR "investment advice" OR "investment recommendation(s)" OR "personal finance" OR "financial planning" OR "retirement planning" OR "financial literacy")`
- R2b: `L AND (finance OR financial OR investment OR investor(s)) AND [ti](uncertainty OR confidence OR calibration OR overconfidence OR overconfident OR hallucination(s))`
- R3: `L AND [ti]("knowledge acquisition" OR "fact learning" OR "factual knowledge" OR "learning new knowledge" OR "new factual knowledge" OR "new facts" OR "knowledge injection" OR "long-tail knowledge" OR "knowledge memorization/memorisation" OR "fact memorization" OR "knowledge boundary/boundaries" OR "temporal knowledge" OR "outdated knowledge" OR "knowledge forgetting" OR "pretraining data frequency")`
- R4a: `L AND [ti]("epistemic diversity" OR "knowledge diversity" OR "whose knowledge" OR homogenization OR homogenisation OR "knowledge coverage" OR "cultural knowledge" OR "epistemic injustice")`
- R4b: OpenAlex backward references and forward citations of seed 1 (W7084854541 = arXiv:2510.04226), publication year 2025–2026.

**Hit counts (arXiv / OpenAlex):**

| Round | v1.0 | after change 1 | v1.1 final | removed by change 1 | removed by change 2 |
|---|---|---|---|---|---|
| R1a | 5,583 / 7,682 | 1,739 / 2,349 | 363 / 335 | 9,177 | 3,390 |
| R1b | 522 / 2,102 | 50 / 290 | 50 / 290 | 2,284 | – |
| R2a | 48 / 472 | 48 / 404 | 48 / 404 | 68 (type filter) | – |
| R2b | 733 / 2,052 | 370 / 1,419 | 63 / 197 | 996 | 1,529 |
| R3 | 843 / 1,673 | 824 / 1,321 | 153 / 203 | 371 | 1,789 |
| R4a | 1,390 / 4,821 | 789 / 677 | 77 / 84 | 4,745 | 1,305 |
| **Total** | **9,119 / 18,802 = 27,921** | **3,820 / 6,460 = 10,280** | **754 / 1,513 = 2,267** | **17,641** | **8,013** |

Counts are raw hits per round; the same paper can appear in several rounds and both sources. Change 1's counts were measured with all its parts together, so the effect of each term swap is not separated.

**Trade-off (for the methods section):** change 2 favours precision over sensitivity — a paper that studies, e.g., calibration without naming it in the title is missed by R1a. Mitigations: R1b/R2a stay title-or-abstract, R4b citation chasing, and the R5 Google Scholar cross-check.

## 2026-11-20 – Run R1–R4 (v1.1), export and de-duplication

- Run: 2026-11-20, 13:09–13:20 CET. arXiv API (ti/abs fields, `submittedDate` 2025-01-01 to 2026-12-31) and OpenAlex API (`title.search` / `title_and_abstract.search`, `publication_year:2025-2026`, `type:article|preprint`). All hits exported (OpenAlex via page paging; cursor paging now requires an API key). R1a arXiv was exported in a first run that stopped on an OpenAlex error before writing its manifest entry (363/363 records, same v1.1 query).
- Seed 1 found by the search: arXiv:2510.04226 in R4a (arXiv), and in R4b as the chasing anchor; screening ID R01687 (batch b039).

| Source | Identified |
|---|---|
| arXiv (R1a 363, R1b 50, R2a 48, R2b 63, R3 153, R4a 77) | 754 |
| OpenAlex (R1a 335, R1b 290, R2a 404, R2b 197, R3 203, R4a 84) | 1,513 |
| **Databases total** | **2,267** |
| Other methods: R4b citation chasing of seed 1 (backward 23 of 49 references; forward 42) | 65 |
| **All records** | **2,332** |
| Duplicates removed (`prepare_records.py`, DOI + title) | 478 |
| **Unique records to screen** | **1,854** (631 from 2025, 1,223 from 2026; 223 without abstract) |

PRISMA screening counts follow after title/abstract screening. Note: `prepare_records.py` de-duplicates database and citation-chasing records together; the PRISMA "other methods" branch is reported from `sr_work/identification.json` and `duplicates.csv`.

## 2026-11-20 – v1.2: narrowed to Frank's chosen rules; re-run, de-duplication, mixed pilot

**Why:** 1,854 unique records (v1.1) were too many for 2–3 RQs. Options and trade-offs: `docs/decisions.md` (entry "Narrowing 1,854 records…"). Frank chose the rules below. The expected total, estimated from the v1.1 records, was 727 unique (≤ 750 ceiling set by Frank), so the search was re-run.

**v1.2 rules** (on top of v1.1; `L` = LLM block; `[ti]` = title only; years 2025–2026; OpenAlex `article|preprint`):
- R1a: v1.1 AND (title or abstract) `(factual OR knowledge OR fact(s) OR memorization OR memorisation OR finance OR financial OR investment(s) OR investor(s) OR stock(s) OR portfolio OR banking OR bank OR trading OR market(s) OR economic(s) OR credit OR robo-advisor OR wealth OR fintech)` (option O2).
- R1b: `[ti]L` instead of title-or-abstract `L`; rest as v1.1.
- R2a: `[ti]L` AND v1.1 finance-advice terms AND (title or abstract) `(uncertainty OR uncertain OR confidence OR calibration OR calibrated OR miscalibration OR entropy OR hedging OR abstain OR abstention OR "I dont know" OR consistency OR consistent OR inconsistency OR reliability OR reliable OR hallucination(s) OR risk(s))`.
- R2b: `[ti]L` instead of title-or-abstract `L`; rest as v1.1.
- R3: v1.1 AND (title or abstract) `(uncertainty OR uncertain OR confidence OR calibration OR calibrated OR miscalibration OR entropy OR hedging OR abstain OR abstention OR "I dont know" OR <finance terms as in R1a>)` (option O2).
- R4a: `[ti]L` instead of title-or-abstract `L`; rest as v1.1.
- R4b: unchanged, complete (references and citing works of seed 1, 2025–2026).

**Hit counts (arXiv / OpenAlex), v1.1 → v1.2:**

| Round | v1.1 | v1.2 | removed |
|---|---|---|---|
| R1a | 363 / 335 | 107 / 100 | 491 |
| R1b | 50 / 290 | 31 / 145 | 164 |
| R2a | 48 / 404 | 18 / 73 | 361 |
| R2b | 63 / 197 | 38 / 106 | 116 |
| R3 | 153 / 203 | 34 / 52 | 270 |
| R4a | 77 / 84 | 47 / 37 | 77 |
| **Databases** | **754 / 1,513 = 2,267** | **275 / 513 = 788** | **1,479** |
| R4b (other methods) | 65 | 65 | 0 |

**Run:** 2026-11-20, same script (`ROUNDS`, v1.1 kept as `ROUNDS_V11`, v1.0 as `ROUNDS_V10`). v1.1 exports and work folder archived in `literature/screening/archive/`.

| PRISMA identification | n |
|---|---|
| Databases: arXiv 275 + OpenAlex 513 | 788 |
| Other methods: citation chasing of seed 1 (backward 23, forward 42) | 65 |
| All records | 853 |
| Duplicates removed | 184 |
| **Records to screen** | **669** (224 from 2025, 445 from 2026; 66 without abstract) |

Seed 1 found by the search (R00559, via R4a); no manual addition needed.
Pilot: b001 = 25 records sampled across all rounds (see `sr_work/pilot_sample.json`); remaining 644 records in b002–b015.
