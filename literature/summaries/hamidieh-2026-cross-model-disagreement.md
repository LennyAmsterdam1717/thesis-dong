# Complementing Self-Consistency with Cross-Model Disagreement for Uncertainty Quantification

**Kimia Hamidieh et al. (2026)** · ICLR 2026 · peer-reviewed · https://arxiv.org/abs/2604.17112
_Paraphrased note by Claude (single reviewer) from abstract, introduction and conclusion/limitations; found via the Google Scholar gap-claim check (other methods); full text checked 2026-11-20._

- **Question:** Self-consistency fails when a model is confidently wrong in every sample - can other models help?
- **Method:** Black-box epistemic-uncertainty term from semantic disagreement across models, combined with intra-model entropy; many models and datasets.
- **Main finding:** Cross-model disagreement is higher on wrong answers exactly where self-consistency is low; the combination beats self-consistency methods.
- **Limitations:** Needs several comparable models; response-level semantic similarity may underperform on some tasks.
- **Relevance for this thesis:** G4 (found by gap-claim check): general-domain answer to homogeneous failure; leaves finance and correlated models open. ICLR 2026.
