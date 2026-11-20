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

## 2026-11-20 – Narrowing 1,854 records toward 200–400 (options; awaiting Frank's choice)

- **Frank:** 1,854 is too many for 2–3 RQs. Keep R2 (a+b), R1b and R4b complete; narrow R1a and R3; aim at 200–400 unique records; afterwards rebuild the pilot as one mixed batch of 25 records sampled across all rounds, including the seed. Do not add b039. No screening and no new search until Frank chooses.
- **Finding:** R1b + R2a + R2b + R4b alone give **1,008 unique records** (R4a adds 125 more). So the 200–400 goal cannot be reached by narrowing R1a and R3 only; the "keep complete" rounds have to be narrowed too, or the goal relaxed. Much of R2a/R1b from OpenAlex is off-topic (stemmed matching: e.g. "financial planning" in infrastructure projects, student trust in ChatGPT).
- **Seed:** seed 1 (R01687) is only in R4a (R4b holds its references/citations, not the seed itself), so it has to be included explicitly if R4a is cut.
- **R1a/R3 options** (unique records added on top of R1b + R2 + R4b + R4a = 1,133); computed from the existing exports and OpenAlex citation counts retrieved 2026-11-20 (`sr_work/citation_counts.json`, `literature/search/narrowing_options.py`):
  - O1 2026 only: +468. Trade-off: loses all 2025 work, including most foundational recent methods.
  - O2 "bridge": R1a kept only with a knowledge or finance term, R3 only with an uncertainty or finance term: +202 (R1a 133, R3 71). Trade-off: keeps the thesis's bridge (certainty × knowledge × finance) but drops general UQ/knowledge methods papers, which become background or come back via citation chasing.
  - O3 surveys + well-cited (≥ 20 citations if 2025, ≥ 5 if 2026): +78 (R1a 58, R3 20); strict (≥ 50 / ≥ 10): +43 (R1a 33, R3 10). Trade-off: citation counts favour 2025, well-known groups and arXiv-visible work; direction 5 (knowledge acquisition) becomes thin (10–20 records); surveys are E2 under the protocol, so this option needs a protocol amendment or would only feed background.
- **Combinations that reach the target** (all relax "keep R1b/R2 complete"; precision filter = an LLM term in the **title**):
  - Y: R1b/R2 with LLM term in title **and** 2026 only; R4b complete; R1a/R3 O3-strict → **394 unique (+ seed)**. Weak spots: R3 = 10 records; no 2025 finance papers.
  - X: R1b/R2 with LLM term in title, R2a also needs an uncertainty/consistency/reliability/risk term; R4b complete; R1a/R3 O3-strict → **490 (+ seed)**.
  - For reference: R1b/R2/R4b with LLM term in title for R1b/R2 = 522 before any R1a/R3 records; R2 + R4b complete with R1b filtered + O3-strict = 915.
- **Not yet decided:** whether R4a stays (Frank's message does not mention it); which option; whether 200–400 or the "complete" rule gives way.

## 2026-11-20 – Frank's narrowing choice (v1.2); search re-run; mixed pilot b001

- **Chosen by Frank:** LLM term in the title for R1b, R2a, R2b and R4a; keep 2025; R2a must also mention uncertainty, consistency or risk (X's rule); R4b complete; R1a and R3 narrowed with O2 (R1a needs a knowledge or finance term, R3 an uncertainty or finance term). Ceiling: re-run only if the expected unique total is ≤ 750.
- **Expected (from v1.1 records):** 727 unique (R1a 152, R1b 184, R2a 82, R2b 122, R3 71, R4a 75, R4b 65 records kept per rule) → ≤ 750, so re-run.
- **Result:** 788 database records (arXiv 275, OpenAlex 513) + 65 citation chasing = 853 → 184 duplicates → **669 unique records**, 15 batches. Seed 1 found by the search (R00559); not added by hand. v1.1 files archived in `literature/screening/archive/` (incl. the unused b001 label sheet).
- **Trade-offs accepted:**
  - LLM term in the title (R1b, R2, R4a): removes OpenAlex noise but misses papers that only name the LLM in the abstract (e.g. "AI advisor" titles).
  - R2a needs an uncertainty/consistency/reliability/hallucination/risk term: drops pure quality evaluations of LLM financial advice (most of them were E4 → background anyway).
  - O2 for R1a/R3: keeps the thesis's link between certainty, knowledge and finance, but drops general UQ methods and general knowledge-acquisition papers that mention neither of the other concepts. Those are needed as background; they can come back via citation chasing and the R5 Google Scholar check.
  - These come on top of v1.1's title-level concept terms (R1a, R2b, R3, R4a): sensitivity is clearly reduced; the corpus is a focused sample, not a complete map. To be stated in the methods.
- **Pilot (Frank's request): one mixed batch of 25 records across all rounds, incl. the seed.** `prepare_records.py` batches in export order, so `tools/make_pilot_batch.py` re-batched `sr_work` before any screening state existed: stratified random sample (random seed 2026; seed record always in; other 24 slots in proportion to unique records per round, min 2): R1a 5, R1b 6, R2a 3, R2b 4, R3 2, R4a 2 + seed, R4b 2 (15 from 2026, 10 from 2025). b001 = the sample; the rest re-batched in ID order (≤ 50 per batch, ≤ 90,000 characters); record IDs unchanged; batch text written with the plugin's `srlib.record_block`. This deviates from the default sr-screener batching and is disclosed in the methods.
- `literature/screening/pilot_labels.csv` = blank labels for b001's 25 records. **No AI screening run.**

## 2026-11-20 – DEVIATION: no human calibration pilot; full title/abstract run

- **Frank decided not to label the pilot.** The calibration pilot (runbook step 2; sr-screener IRON RULE 2) is skipped through sr-screener's recorded override: `build_workflow.py ta --jobs all --pilot-override "<reason>"`; reason stored in `literature/screening/sr_work/pilot_override.json` and reported automatically in the methods text. Consequence: **no human calibration pilot** — the AI reviewers' reading of the protocol was not checked against human labels before the full run, and the seed check happens in the full run instead.
- **Compensation (Frank):** after screening, a verification sheet with a random sample of 20 exclusions and 10 inclusions, each with the AI's one-line reason; Frank marks agree/disagree. Agreement is reported in the methods. **Stop condition:** if Frank disagrees with any exclusion, Claude stops before full text.
- **Run:** all 15 batches (669 records), Reviewer A + Reviewer B (`academic-research-skills:screening-reviewer-agent`, Sonnet, blinded, read-only), adjudication of conflicts, QC recheck of joint exclusions + near-misses. Cost estimate from `build_workflow.py`: ~30 reviewer calls + retries + one adjudication call per batch with conflicts + recheck calls. Workflow tool not available in this session → Agent-tool path (`--emit-prompts`, one call per prompt file, returns saved in `sr_work/decisions/`).
- b001 stays the stratified mixed batch (it is simply the first of the 15 batches now); `pilot_labels.csv` stays blank and is not used.

## 2026-11-20 – Title/abstract screening complete; verification sheet for Frank

- **Run (no human pilot, recorded override):** 669 records, 15 batches; Reviewer A + B (Sonnet, `screening-reviewer-agent`, blinded) = 30 calls; 20 conflicts → 9 adjudicator calls; QC recheck of 307 exclusions (random sample of 100 joint exclusions, seed 2026, + all near-miss exclusions) = 8 calls. All returns saved verbatim in `literature/screening/sr_work/decisions/` (extracted from the subagent hand-backs by `tools/extract_returns.py`, never retyped).
- **Agreement A vs B (advance vs exclude):** n = 669, observed 97.0 %, Cohen's κ = 0.939, PABAK = 0.94, 20 conflicts.
- **Final:** 197 include + 96 unclear = **293 advance to full text**; **376 excluded** (E2 81, E3 35, E4 71, E5 187, E9 2). Decided by A+B 643, adjudicator 19, QC recheck 7 (QC advanced 7 joint exclusions). Seed 1 (R00559) included by both reviewers.
- Outputs: `literature/screening/Screening_TA/` (CSV log — openpyxl not installed —, RIS groups, PRISMA counts, methods text, literature corpus).
- **Note on PRISMA:** `build_outputs.py` lists the 65 citation-chasing records inside the "databases" box. In the thesis flow diagram they go in the "other methods" branch (identified via citation searching: 65); databases = 788.
- **Verification sheet (Frank's compensation for the skipped pilot):** `literature/screening/verification_sheet.csv` — 20 random final exclusions + 10 random final inclusions (seed 2026, mixed order), each with the AI's one-line reason; Frank fills `agree_disagree`. `tools/verification_agreement.py` computes the agreement for the methods. **Stop rule:** if Frank disagrees with any exclusion, Claude stops before full text.
- Note: the 96 "unclear" records also advance but are not in the inclusion sample (Frank asked for inclusions).

## 2026-11-20 – Verification sample checked by AI, not by Frank

- **Decision:** Frank delegated the 30-record verification sample (`literature/screening/verification_sheet.csv`) to Claude Opus 5.5 (claude.ai session), with permission to judge scope. A first attempt by Frank (18/30 disagree, mostly on records that are clearly in or out of scope) was not used. The sheet has a `checked_by` column saying who checked it.
- **Result:** 28/30 agree; exclusions 18/20, inclusions 10/10. Disagreements on two exclusions: **R00334** (*Expressed distress and portfolio risk in LLM investment advice*, no abstract; protocol exception (a), finance evaluation mentioning risk → unclear) and **R00615** (*The shrinking landscape of linguistic diversity in the age of LLMs*, no abstract; case (d) → unclear). Code note: R00221 is better coded E2 than E3 (decision unchanged).
- **Consequence:** the stop rule fires (disagreement with an exclusion). Suggested handling: advance R00334 and R00615 to full text as overrides, and check whether other no-abstract finance records mentioning risk were excluded under E4 against exception (a).
- **Methods consequence:** this is an AI check, not a human verification. With the skipped calibration pilot, **no screening decision has been checked by a human**; `methods-draft.md` states this as a limitation. Frank can still remove it by checking a sample himself later.

## 2026-11-20 – Overrides after verification; exception (a) recheck

- **Frank's instruction:** advance R00334 and R00615 (verification disagreements) as overrides; check other excluded records without an abstract, and finance records mentioning risk, against protocol exception (a) and advance those too.
- **Recheck (single reviewer: Claude Opus 5.5, main session; title/abstract only):** 46 excluded records without an abstract (judged by title under exception (a) and cases (b)/(d)) and 49 E4 records whose abstract mentions risk/reliability/consistency/uncertainty/confidence/hallucination. Rule applied, consistent with Frank's R00334 override: an LLM evaluation (incl. finance) where risk, reliability or consistency **of the LLM's own output** is mentioned → unclear; risk only as the *investor's* risk tolerance, retrieval/verification fixes for hallucination, and LLM-as-measurement-tool papers stay excluded.
- **Advanced (13 by Claude + 2 by Frank = 15 overrides, `literature/screening/overrides.csv`):** no abstract: R00178, R00349, R00417, R00448, R00466, R00470, R00471; finance with abstract: R00325, R00328, R00329, R00341, R00353, R00366; Frank: R00334, R00615.
- **Caveat:** `build_outputs.py` reports these as "human overrides"; 13 of the 15 are AI judgments (labelled in the `by` column). Methods text must say so.
- **New totals:** 197 include + 111 unclear = **308 advance**; 361 excluded.

## 2026-11-20 – DEVIATION: full-text stage replaced by charting + targeted full-text check (Frank)

- **Instead of** full-text screening of all advanced records (runbook step 4) and a citation check of every included paper (step 5):
  1. **Charting** of all 308 advanced records from title/abstract into `literature/charting.csv` (directions, concept, finance flag, study type, models — keyword-assisted, see the file header).
  2. **Gap analysis** (`research-questions/gap-analysis.md`) written from the charting table.
  3. **Single-reviewer full-text check** (Claude, go-light; proof-of-reading rule from `ft_protocol.md` applies) **plus citation check** only for the **30–50 papers used as evidence** for gaps, RQs and the supervisor email.
  4. Only those papers go into `literature/papers.csv`.
- **Consequences for reporting:** the other advanced records are *not* full-text assessed and are not "included studies"; the PRISMA flow stops at "reports sought" for them, and the review is reported as a scoping/integrative map with a targeted evidence set, not as a systematic review with a full-text-confirmed corpus.
- Then the runbook continues from step 6 (summaries) onward, including the R5 Google Scholar cross-check before the email draft.
