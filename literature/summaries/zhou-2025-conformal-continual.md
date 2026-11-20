# Robust Uncertainty Quantification for Self-Evolving Large Language Models via Continual Domain Pretraining

**Xiaofan Zhou et al. (2025)** · arXiv preprint · preprint · https://arxiv.org/abs/2510.22931
_Paraphrased note by Claude (single reviewer) from the abstract, introduction and discussion/limitations; full text checked 2026-11-20._

- **Question:** Statistical guarantees for LLM answers when the model keeps being trained on new domains.
- **Method:** Proposes AR-NECP, a conformal prediction method that reweights calibration data by estimated domain distribution and adds label-conditional abstention; experiments under continual domain pretraining.
- **Main finding:** Gives stronger coverage guarantees and more informative prediction sets than standard conformal methods under domain shift.
- **Limitations:** Variance in per-domain test estimates; calibration answers must be re-sampled after each fine-tuning stage (cost).
- **Relevance for this thesis:** G1: uncertainty guarantees break when knowledge is updated - relevant to financial facts that change.
