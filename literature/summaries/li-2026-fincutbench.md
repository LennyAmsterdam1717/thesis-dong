# FinCutBench: A Continually Updated Benchmark for Measuring the Temporal Boundaries of LLM Financial Knowledge

**Siyuan Li et al. (2026)** · arXiv preprint · preprint · https://arxiv.org/abs/2611.11588
_Paraphrased note by Claude (single reviewer) from abstract, introduction and conclusion/limitations; found via the Google Scholar gap-claim check (other methods); full text checked 2026-11-20._

- **Question:** How far does a fixed model's financial knowledge extend over calendar time (parametric look-ahead bias)?
- **Method:** Continually updated monthly benchmark: 9,000 Chinese/English multiple-choice questions (Jan 2023-Sep 2026), Chinese and U.S. markets; knowledge profiles from closed-book accuracy, boundary detection by change-point and curve fitting.
- **Main finding:** Locates per-model temporal boundaries of financial knowledge; downstream effects differ by task and market.
- **Limitations:** Multiple-choice guessing; first-public dates hard to verify; partly generated questions; measures accuracy, not model confidence (only statistical confidence intervals; an abstain option exists).
- **Relevance for this thesis:** G1 (key, found by gap-claim check): the temporal boundary of financial knowledge is measured by accuracy - calibration and confidence over fact age remain open. Possible data source for RQ2.
