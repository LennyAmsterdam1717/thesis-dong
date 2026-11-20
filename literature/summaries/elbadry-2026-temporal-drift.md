# The Geometry of Forgetting: Temporal Knowledge Drift as an Independent Axis in LLM Representations

**Rania Elbadry et al. (2026)** · arXiv preprint · preprint · https://arxiv.org/abs/2605.09195
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Asks why LLMs give outdated answers with confidence and why existing detectors miss it.
- **Method:** Probing study on six instruction-tuned LLMs: linear probes on the residual stream, suppression/amplification interventions on a controlled split.
- **Main finding:** Whether a stored fact has changed since training sits on its own direction in the residual stream, at right angles to both correctness and uncertainty; drift-trained probes reach 0.83-0.95 AUROC while correctness/uncertainty methods stay near chance.
- **Limitations:** Probing study; some models dropped from interventions due to filtering constraints.
- **Relevance for this thesis:** G1: confidence signals cannot see staleness - core motivation for time-sensitive financial facts.
