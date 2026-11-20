# The Alignment Tax: Response Homogenization in Aligned LLMs and Its Implications for Uncertainty Estimation

**Mingyi Liu et al. (2026)** · arXiv preprint · preprint · https://arxiv.org/abs/2603.24124
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Why do sampling-based uncertainty methods fail on aligned models?
- **Method:** TruthfulQA, GSM8K and others; cluster statistics across 10 samples; base-vs-instruct and training-stage ablations; proposes a cascade of signals.
- **Main finding:** Aligned models often give a single semantic cluster (e.g. 28.5% vs 1.0% for base), making sampling-based UQ blind (AUROC 0.5) while token entropy keeps some signal.
- **Limitations:** Single independent author; architectural proposal preliminary.
- **Relevance for this thesis:** G4 (key): homogeneity turns agreement into a false confidence signal.
