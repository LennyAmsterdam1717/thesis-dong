# Runbook: what happens when Frank says "go" / "go light"

_Prepared 2026-11-20. Claude (Claude Code in VS Code, with the `academic-research-skills` plugin) follows this top to bottom. Commit and push after every step._

## What "go" means

By saying **"go"**, Frank confirms the protocol as last drafted, approves the screening cost (Sonnet reviewer calls for pilot, full run, adjudication, QC recheck, and dual full-text review) and asks Claude to continue the whole brief without check-ins, except at the stop conditions below.

**"go light"** means the same, except the full-text stage is a **single-reviewer** check by Claude, disclosed as such in `literature/methods-draft.md` and `docs/decisions.md`.

## Steps

1. **Protocol and config.** Draft `literature/screening/screening_protocol.md` (PCC, exclusion codes, `[proposed]` rules) and `screening_config.json` (same structure as the template, `conflict_policy: "adjudicate"`, `agent_type: academic-research-skills:screening-reviewer-agent`, personas and QC keywords below). **STOP:** Frank confirms.
2. **Calibration pilot.** Frank labels batch b001 (25 records, including the seed) independently in `pilot_labels.csv`. Reviewer A and B (Sonnet, `screening-reviewer-agent`) screen the same batch: `build_workflow.py ta --jobs pilot --batches b001 --emit-prompts ...` → save returns in `sr_work/decisions/` → `merge_decisions.py --from sr_work/decisions --overrides overrides.csv --pilot-labels pilot_labels.csv`. The full run waits until the AI misses none of the records Frank advanced.
3. **Full title/abstract run.** `--jobs all` → A + B → merge → `--jobs pending` (adjudication) until no conflicts remain → `--jobs recheck` (QC recheck of joint exclusions + near-misses) → `build_outputs.py --work sr_work --out Screening_TA --config screening_config.json`. PRISMA counts into `literature/search-log.md`; E4 papers into `literature/background.md`. Keep the automatic methods text in `Screening_TA/TA_methods_selection.md`.
4. **Full text.** Download PDFs into `literature/screening/fulltext/` (git-ignored), `prepare_fulltext.py`, write `ft_protocol.md`. **go** = dual AI review (+ adjudication), `build_outputs.py --stage ft`; **go light** = single-reviewer check by Claude, logged separately and disclosed. Publisher-only papers are reported as "not retrieved", not excluded.
5. **Citation check.** `academic-paper` citation-check on every included paper (title, authors, year, venue, DOI/arXiv link vs arXiv API or DOI resolver); raw results in `literature/citation-check/`. Only passing papers go into `literature/papers.csv`, all columns filled.
6. **Summaries.** One paraphrased note per key paper in `literature/summaries/<firstauthor-year-keyword>.md`, including the seed paper(s).
7. **Research questions.** `research-questions/gap-analysis.md` (themes + 5–8 gaps, each tied to papers) → `rq-candidates.md` (3–5 RQs: RQ, sub-questions, gap, evidence with links, method, data, 8-month feasibility, why Accenture) → `rq-shortlist.md` (top 2–3 + rationale).
8. **Verify the gap claims.** Google Scholar cross-check (R5) on every "nobody has done X" claim; read the abstracts (and where they matter, full texts) of any missed paper; screen them through the "other methods" branch. Revise gaps/RQs if a claim falls.
9. **Supervisor email.** `research-questions/email-dong-draft.md`: max 3 RQs, main candidate first, each backed by 1–2 papers with a link and one line on relevance. Clearly mark papers that have not passed the citation check.
10. **Wrap-up.** Update `README.md`, `docs/decisions.md`, `docs/timeline.md`; final commit and push; short summary for Frank (number of papers, top RQs, open questions).

## Config content for this topic

- **Reviewer A persona:** "an NLP researcher with expertise in uncertainty quantification, calibration and knowledge in large language models, who also follows LLM use in finance".
- **Reviewer B persona:** "a literature-review methodologist experienced in scoping and integrative reviews in computer science".
- **QC near-miss keywords:** uncertainty, confidence, calibration, overconfiden*, semantic entropy, financial advice, knowledge acquisition, fact learning, epistemic.

## Stop conditions (Claude stops and asks)

- The pilot misses a record Frank advanced.
- Fewer than 15 papers survive full text and citation check.
- A failed citation check changes an RQ's evidence base.
- Any step would push PDFs, Word files or other git-ignored material.

## Frank still has to do

- **Verify the final included set** (every advanced record plus a sample of exclusions) before the counts are final.
