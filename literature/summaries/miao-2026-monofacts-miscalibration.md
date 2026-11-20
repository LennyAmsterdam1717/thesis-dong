# Hallucination, monofacts, and miscalibration: An empirical investigation

**Miranda Muqing Miao et al. (2026)** · Proceedings of the National Academy of Sciences (2026) · peer-reviewed · https://doi.org/10.1073/pnas.2533582123 ; https://arxiv.org/abs/2502.08666
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Empirically tests the theory that hallucination is bounded by the monofact rate minus miscalibration.
- **Method:** Controlled training of n-gram models and fine-tuned transformers on generated fact distributions; selective upweighting of facts.
- **Main finding:** The three-way relation holds in practice; upweighting a subset of facts makes the model overconfident on them and pulls probability away from the uncertain tail where hallucinations come from.
- **Limitations:** Mechanism partly hypothesised; intervention upweights random subsets.
- **Relevance for this thesis:** G2 (key): direct link between how often a fact was seen in training, calibration and hallucination. PNAS.
