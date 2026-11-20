# Thesis (alternative topic) – How certain are LLMs, and how do they acquire knowledge?

**Topic in one paragraph.** People increasingly ask LLMs for financial advice, and LLMs usually answer with high confidence even though markets are inherently uncertain. This thesis asks how certain LLMs really are, and how that (un)certainty can be measured: verbalised confidence, token probabilities, sampling consistency, semantic entropy and claim-level uncertainty, and whether stated confidence matches accuracy (calibration). A second, linked direction asks how LLMs acquire factual knowledge during pre-training and fine-tuning (frequency and long-tail effects, learning new facts, hallucination), and whether *how* a fact was learned explains *how sure* the model is about it. The bridge is that confidence in an answer may depend on how well the underlying knowledge was acquired, and financial facts change over time.

## People

- **Student:** Frank (Lenny) Pam – MSc Artificial Intelligence, Utrecht University
- **Supervisor (UU):** Dong Nguyen – daily supervisor and first examiner; meeting date: _to be set_
- **Internship:** Accenture, Technology Strategy & Transformation, from **4 January 2027**

## Key facts

- Alternative topic next to the main one (process mining for agentic AI, Dr. Xixi Lu; repo `Thesis-Process-mining`, used here as the structural template only).
- 8-month thesis preferred by UU (45 EC); Accenture internships are capped at 6 months, 2-month extension requested.
- Public or cheaply obtainable data only; no client data. Accenture-internal data optional.
- Method must be defensible (experiment, measurement study, public-dataset analysis).
- GenAI may be used, as long as Frank can explain everything it produced.

**Seed paper 1 (from Dong Nguyen):** Wright et al. (2026), *What and Whose Knowledge? Measuring Epistemic Diversity in Large Language Models*, EMNLP 2026 – <https://aclanthology.org/2026.emnlp-main.1542.pdf> (citation check pending).

## Repository contents

| Path | What |
|---|---|
| `CLAUDE.md` | Workflow rules for Claude Code |
| `.claude/settings.json` | Enables the `academic-research-skills` plugin for this project |
| `docs/decisions.md` | Append-only log of every scope/method choice |
| `docs/runbook-go.md` | What happens on "go" / "go light" |
| `docs/timeline.md`, `docs/next-steps.md` | Planning |
| `docs/meetings/` | One note per supervisor meeting |
| `literature/search-plan.md` | Draft search strings R1–R4 |
| `literature/search-log.md` | Search rounds + PRISMA 2020 counts |
| `literature/papers.csv` | Citation-checked papers only |
| `literature/screening/` | SR-Screener protocol, config, records, logs |
| `literature/summaries/` | One paraphrased note per key paper |
| `literature/background.md` | Relevant papers outside the review corpus |
| `literature/methods-draft.md` | Methods text for the literature selection |
| `literature/citation-check/` | Raw citation-check results |
| `research-questions/` | Gap analysis, RQ candidates, shortlist, supervisor email |
| `experiments/` | Pilots (later) |

## Status (2026-11-20)

- ✅ Plugin checked; protocol v1.0 confirmed ("go light"); search v1.2: 669 records screened.
- ✅ Title/abstract screening by AI reviewers (no human pilot — recorded deviation); 15 overrides (**2 by Frank, 13 AI judgments by Claude**, although the plugin labels all "human"); 308 advanced, 361 excluded.
- ✅ Charting of 308 records; gap analysis v0.3; targeted single-reviewer full-text check + citation check of the evidence set: **33 papers** in `literature/papers.csv` (30 from the search, 3 via the Google Scholar gap-claim check); 6 not retrieved.
- ✅ Google Scholar cross-check (R5) done; RQs narrowed (`research-questions/rq-shortlist.md`): **RQ1** acquisition route × confidence on financial facts (main), **RQ2** confidence on financial facts that change, **RQ3** uncertainty for advice (stretch).
- ✅ Email draft to Dong Nguyen: `research-questions/email-dong-draft.md` (**not sent**).
- ⏳ Frank: read the email draft and the method caveats in `literature/methods-draft.md`; no screening decision has been verified by a human (Frank may still check a sample to lift this limitation); set the meeting date.
