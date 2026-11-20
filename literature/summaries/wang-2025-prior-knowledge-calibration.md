# Towards Objective Fine-tuning: How LLMs’ Prior Knowledge Causes Potential Poor Calibration?

**Ziming Wang et al. (2025)** · ACL 2025 (Long Papers), pp. 14830-14853 · peer-reviewed · https://doi.org/10.18653/v1/2025.acl-long.722
_Paraphrased note by Claude (single reviewer) from abstract, introduction and conclusion/limitations; found via the Google Scholar gap-claim check (other methods); full text checked 2026-11-20._

- **Question:** Why are fine-tuned LLMs poorly calibrated, and what role does prior knowledge play?
- **Method:** Fine-tuning experiments separating training data the model already knows from new data; proposes CogCalib, a real-time cognition-aware calibration during fine-tuning.
- **Main finding:** Data aligned with the model's prior knowledge (very common in real-world fine-tuning) induces overconfidence, while new knowledge behaves differently; CogCalib improves calibration without hurting performance or adding deployment cost.
- **Limitations:** Only some models and settings studied (Limitations); general domain.
- **Relevance for this thesis:** G2 (key, found by gap-claim check): the general-domain link between what a model already knows and confidence after fine-tuning. RQ1 must build on it and add route comparison and finance.
