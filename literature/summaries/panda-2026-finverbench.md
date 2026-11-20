# FinVerBench: Benchmark Validity and Calibration in Large Language Model Financial Statement Verification

**Silu Panda et al. (2026)** · arXiv preprint · preprint · https://arxiv.org/abs/2605.29586
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Can LLMs verify the numerical consistency of financial statements, and how valid are such benchmarks?
- **Method:** FinVerBench from SEC 10-K XBRL filings of 43 S&P 500 firms; four error categories; 14 model runs.
- **Main finding:** Many models detect injected errors but cannot refrain from flagging clean statements; performance spans a wide spectrum of false-positive behaviour.
- **Limitations:** 'Calibration' here means false-positive restraint, not probability calibration; single author.
- **Relevance for this thesis:** G6 (finance, weak): nearest finance benchmark; shows the gap for probability calibration.
