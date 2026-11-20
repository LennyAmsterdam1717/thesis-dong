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
