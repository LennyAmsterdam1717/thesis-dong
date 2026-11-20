# Decisions log

Append new entries at the bottom; do not overwrite earlier ones.

## 2026-11-20 – Repository set-up and draft review design (to be confirmed)

- **Decision:** New working repository for an alternative thesis topic with supervisor candidate Dong Nguyen, using the same research workflow and agents as `Thesis-Process-mining` (structure only; no content copied).
- **Set-up note:** the scaffold was created in a claude.ai session where the `academic-research-skills` plugin is **not** available. No search, screening or citation check was done there. All literature work runs in Claude Code (VS Code), where the plugin is installed at user level. `.claude/settings.json` records the plugin as `academic-research-skills@academic-research-skills` (marketplace and plugin name from the plugin repo's `.claude-plugin/marketplace.json`, v3.24.4); confirm the id with `/plugin` and correct it if Frank's install uses a different marketplace name.
- **Review form (draft):** integrative review in ARS `lit-review` mode, used for a scoping purpose: map the field and find gaps for 2–3 research questions. PRISMA 2020 counts logged per round in `literature/search-log.md`.
- **Year range (proposed, Frank decides):** **2024–2026** for the review corpus, with older foundational papers (e.g. semantic entropy, early calibration and knowledge-probing work) as background in `literature/background.md`. Why: uncertainty quantification and knowledge acquisition in LLMs have a large 2023–2025 literature, so a 2026-only window (as in the process-mining review) would miss most of the field. Not widened later without Frank's approval.
- **Sources:** peer-reviewed venues and arXiv preprints, each labelled as one or the other; every paper needs a working DOI or arXiv link.
- **Eligibility (PCC, draft):** Population = LLMs (chat assistants, agents, base models). Concept = measuring uncertainty, confidence or calibration of LLM outputs, OR how LLMs acquire or represent factual knowledge. Context = financial advice prioritised; general-domain methods included when transferable.
- **Exclusion codes (proposed):** E1 year · E2 publication type · E3 not about LLMs · E4 finance-only without any uncertainty/knowledge angle (kept as background) · E5 no measurement or analysis of uncertainty/knowledge · E9 other.
- **Search rounds (proposed):** R1 uncertainty quantification and calibration of LLMs; R2 LLMs and financial advice (incl. confidence and risk); R3 knowledge acquisition and fact learning; R4 epistemic diversity / knowledge representation + citation chasing from the seed paper(s); R5 Google Scholar cross-check (browser panel, Frank solves CAPTCHAs), missed papers screened via the "other methods" branch.
- **Working list of directions (for the `directions` column of `papers.csv`):**
  1. uncertainty quantification methods for LLM outputs
  2. calibration and overconfidence (verbalised vs actual)
  3. LLMs for financial advice: quality, risk, consistency
  4. user perception of and trust in LLM confidence
  5. knowledge acquisition during pre-training / fine-tuning
  6. epistemic diversity and what knowledge LLMs represent
  7. evaluation datasets and benchmarks (esp. finance)
- **Seed paper 1:** Wright et al. (2026), *What and Whose Knowledge? Measuring Epistemic Diversity in Large Language Models*, EMNLP 2026 main (given by Dong Nguyen). Citation check pending, like any other paper.
- **Open for Frank:** year range; keep both directions A and B or focus on one; seed paper 2; Dong Nguyen's role (daily supervisor / first examiner) and meeting date.

## 2026-11-20 – Plugin check in Claude Code (set-up §8 step 2, part 1)

- **Checked:** `academic-research-skills@academic-research-skills` is installed at user level, **v3.24.3** (commit a6da64f); the id matches `.claude/settings.json`, so no correction needed. An update to v3.24.4 is available (`/plugin update academic-research-skills`); the scaffold note referred to v3.24.4.
- `sr-screener` skill loads; `prepare_records.py`, `build_workflow.py`, `merge_decisions.py`, `build_outputs.py`, `prepare_fulltext.py` all run (`--help`) under Python 3.14.7. Agent `academic-research-skills:screening-reviewer-agent` is available.
- **Note:** `openpyxl` is not installed, so `build_outputs.py` would write the screening log as CSV instead of `TA_screening_log.xlsx`. Optional; `pip install openpyxl` if Frank wants the Excel log.

## 2026-11-20 – Frank's answers to the open questions

- **Year range: 2025–2026** (not the proposed 2024–2026). Papers published before 2025 do not enter the review corpus; foundational/earlier work (e.g. semantic entropy 2023/2024, early calibration and knowledge-probing work) goes to `literature/background.md`. Applies to the year of the first public version (arXiv v1 or publication, whichever is earlier). Not widened without Frank's approval.
- **Directions: keep both A (LLM certainty: uncertainty, calibration, financial advice) and B (knowledge acquisition / epistemic diversity).** R1–R4 as planned.
- **Seed paper 2: none yet.** The review runs with seed 1 (Wright et al., 2026) only; Claude may propose candidates after R1 for Frank to choose.
- **Dong Nguyen: daily supervisor and first examiner** (UU). Meeting date still to be set.

## 2026-11-20 – Draft screening protocol v0.1, config and R1–R4 search plan (runbook step 1; awaiting Frank)

- **Files:** `literature/screening/screening_protocol.md` (v0.1 DRAFT), `literature/screening/screening_config.json`, `literature/search-plan.md`. Nothing searched or screened.
- **Eligibility:** PCC as drafted earlier, with concept A (LLM certainty) and concept B (LLM knowledge) written out as *counts / does not count / unclear* lists. Exclusion codes renumbered into checking order: E1 year · E2 publication type · E3 not LLMs · E4 finance without concept (to background) · E5 concept missing · E9 other.
- **Config:** `conflict_policy: adjudicate`, Sonnet for every role, `agent_type: academic-research-skills:screening-reviewer-agent`, personas and near-miss keywords from the runbook (two groups, LLM + concept), QC sample 100 (seed 2026), seed 1 by title (DOI left empty until the citation check).
- **`[proposed]`, open for Frank:** (1) year rule: year shown in the record (venue year; arXiv-only = first-submission year). This replaces the "first public version, whichever is earlier" wording in the previous entry, which Claude added without Frank deciding it. (2) Surveys/reviews excluded as E2 but kept for background and citation chasing. (3) Knowledge-editing papers that report only edit success do not count for concept B. (4) Encoder-only classifiers do not count as LLMs. (5) Sources: arXiv API + OpenAlex API (Scopus optional). (6) Pilot size: runbook says b001 = 25 records; the config's batch size is 50, so b001 would be 50 unless set to 25.

## 2026-11-20 – Protocol v1.0 confirmed; "go light"; proof-of-reading rule for full text

- **Confirmed by Frank:** proposed points 1–4 as drafted (year = year shown in the record, arXiv-only = first-submission year; surveys/reviews = E2 but kept for background and citation chasing; edit-success-only knowledge-editing papers and encoder-only classifiers do not count; sources = arXiv API + OpenAlex API, Scopus not used). Point 5: **keep 50 records per batch** (so pilot batch b001 has up to 50 records, not 25 as in the runbook). `screening_protocol.md` frozen as **v1.0**; `search-plan.md` v1.0.
- **Run mode: "go light"** — runbook as written, with the full-text stage as a **single-reviewer check by Claude**, disclosed in `literature/methods-draft.md` and here.
- **Full-text proof-of-reading rule (Frank, 2026-11-20):**
  - Every full-text decision includes a `last_section` field: a short paraphrase (max 20 words) of something from the paper's limitations, discussion or conclusion, with its page marker.
  - After each batch, every decision is checked. A decision fails if `last_section` is missing or empty, or if its page marker is not in the last third of the report (counting pages before the references).
  - Failed decisions are re-run, at most twice. If one still fails, it is flagged for Frank and not counted (stays pending).
  - Also recorded in the amendment log of `literature/screening/ft_protocol.md` and stated in the full-text methods text.

## 2026-11-20 – Search tightened to v1.1; search run; pilot batch b001 prepared

- **Volume check failed for v1.0:** 27,921 raw hits (arXiv 9,119; OpenAlex 18,802) vs the ~2,500 ceiling. Frank (stepping away) asked Claude to tighten without waiting, keep 2025–2026, keep both sources and all 7 directions. (A first version of that message asked for "agent" and "trace/process" terms and 2026 only; Frank corrected it: those were for the process-mining project. Not applied.)
- **Changes:** (1) narrower terms and OpenAlex types `article|preprint`; (2) concept terms required in the title for R1a, R2b (concept block), R3, R4a. R1b and R2a stay title-or-abstract. Old/new strings and per-change counts in `literature/search-log.md`. All 7 directions keep at least one round (1, 2 → R1a; 4 → R1b; 3, 7 → R2a/R2b; 5 → R3; 6 → R4a/R4b).
- **Result:** 2,267 database records + 65 citation-chasing records (R4b) → 478 duplicates → **1,854 unique records**, 43 batches of ≤50. Seed 1 found (R01687, batch b039).
- **Known trade-off:** title-only concept terms lower sensitivity; mitigated by R4b and the R5 Google Scholar check. To be stated in the methods.
- **OpenAlex without API key:** cursor paging now needs a key, so the script uses page paging; heavy boolean queries are paced at 1 per 2.5 s. No personal data sent.
- **Pilot:** `literature/screening/pilot_labels.csv` holds blank labels for batch **b001 (R00001–R00050)** for Frank. No AI screening has been run on b001 or any other batch. Note: b001 is the first 50 records in input order, so all come from R1a (uncertainty, arXiv/OpenAlex, mostly early 2025) and the seed is not in it (it is in b039). Frank decides whether to add b039 (or another spread of batches) to the pilot.
