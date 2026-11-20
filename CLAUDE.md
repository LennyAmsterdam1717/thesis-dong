# Thesis (alternative) – LLM certainty in financial advice & knowledge acquisition

See README.md for the topic, people and key facts.

## Before any literature work

Check that the **academic-research-skills** plugin is installed and enabled (`/plugin`; project setting in `.claude/settings.json`). If it is not available, stop and tell Frank. Do not substitute other tools for the plugin's agents.

## Literature workflow

Use the **academic-research-skills** plugin for all literature work:

1. **Search** – `deep-research` in **lit-review** mode.
2. **Screen** – `sr-screener` (title/abstract, then full text). Log the PRISMA 2020
   counts for every search round in `literature/search-log.md`.
   - Reviewers: `academic-research-skills:screening-reviewer-agent` on **Sonnet** – Reviewer A and B (blinded, different personas, read-only, no web), a third reviewer for adjudication, a senior reviewer for the QC recheck of joint exclusions.
   - Scripts: `build_workflow.py ta --jobs pilot|all|pending|recheck --batches ... --emit-prompts ...`; `merge_decisions.py --from sr_work/decisions --overrides overrides.csv --pilot-labels pilot_labels.csv`; `build_outputs.py --work sr_work --out Screening_TA --config screening_config.json` (and `--stage ft`); `prepare_fulltext.py`.
3. **Verify** – run the `academic-paper` **citation-check** on every paper (title, authors, year, venue, DOI/arXiv link against the arXiv API or DOI resolver). A paper goes into `literature/papers.csv` only after it passes.

Never add a paper to `papers.csv` from memory or from a search result alone.

## Rules

- PDFs and Word files are git-ignored (see .gitignore); never commit papers or personal notes.
- Commit and push after every completed step, so Frank can follow progress on GitHub.
- Log every scope or method choice in `docs/decisions.md` (append-only).
- Do not widen the year range without Frank's approval.

## Pending run

If Frank says **"go"** or **"go light"**, follow `docs/runbook-go.md` step by step.
