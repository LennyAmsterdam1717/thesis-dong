# Gap analysis

_Draft v0.1, 2026-11-20. Written from `literature/charting.csv` (308 records advanced at title/abstract, search v1.2, 2025–2026). Paper references are screening IDs (Rxxxxx) from the charting table. Status of every cited paper: **TA = title/abstract only; full-text and citation check pending**. After the targeted full-text + citation check (evidence set, see bottom) this file is revised and IDs are replaced by citation keys from `literature/papers.csv`._

## What the corpus looks like

308 advanced records (197 include, 111 unclear). Keyword-assisted tags (noisy, see `charting.csv`): UQ methods ~135, calibration/overconfidence ~139, user perception/trust ~111, knowledge acquisition/boundaries ~44, epistemic diversity/whose knowledge ~27, datasets/benchmarks ~153. Finance-specific records (hand-checked): roughly 40, most from R2 (advice evaluations, hallucination in financial QA, confidence for financial decisions).

## Themes

- **T1 – UQ methods for LLM outputs (largest theme).** Token/logit-based, sampling/consistency-based (semantic entropy and variants), probe/hidden-state, verbalized, claim-level for long-form text, conformal guarantees. A strand of 2025–26 *critical evaluations* shows the methods break outside clean factual QA: under ambiguity (R00039), in RAG (R00012), when uncertainty has several sources (R00066), and because they measure agreement between samples rather than correctness (R00077, R00104). Large comparative studies: R00016 (80 models), R00037, R00079 (46 estimators vs hallucination).
- **T2 – Calibration and overconfidence.** Verbalized overconfidence is systematic (R00003, R00063 mechanistic, R00118 competing biases, R00092 stable high-confidence errors); more reasoning can worsen calibration (R00025).
- **T3 – People and LLM confidence.** Users over-rely on confident LLMs, across languages (R00159); gap between what LLMs know and what people think they know (R00173); confident wrong assistants pull users along (R00172); confidence, not accuracy, drives trust in commercial LLMs (R00203); uncertainty expressions shift reliance over repeated use (R00209).
- **T4 – LLMs and financial advice.** Advice is sensitive to irrelevant input changes (R00319 repeated risk-tolerance answers), to country/language (R00340), converges across models (R00333), shows biases and portfolio risks (R00328, R00334); finance-specific confidence work is recent and small: confident hallucinations in financial QA detectable from internal states (R00407), naming an asset inflates conviction (R00475), the value of a confidence score depends on the financial decision rule that consumes it (R00411), calibration of financial predictions (R00431), benchmark validity and calibration in financial statement verification (R00404).
- **T5 – How LLMs acquire and hold factual knowledge.** Knowledge boundaries (many 2025–26 papers, e.g. R00490, R00498), knowledge injection by fine-tuning (R00510; finance: R00537 SFT vs CPT, R00413, R00341), memorization capacity (R00625), temporal drift and outdated facts (R00508, R00530), popularity/frequency effects (R00014), training-data roots of hallucination and miscalibration (R00002 monofacts; R00047 tracing verbalized confidence to training data; R00049 knowledge probing through calibration).
- **T6 – Epistemic diversity and homogenization.** Seed R00559 (what and whose knowledge), R00584, R00564 (diversity across models mitigates knowledge collapse), R00562 (Artificial Hivemind), and the bridge to T1: alignment-induced homogenization makes sampling-based UQ blind (R00571).

## Gaps (each tied to papers; all TA-level until checked)

**G1 – Confidence on facts that change: time-sensitive (financial) knowledge.**
LLMs answer outdated facts confidently, and temporal drift is encoded separately from correctness and uncertainty, so standard UQ cannot see it (R00508); outdated knowledge is unevenly distributed across regions (R00530); in a regulated domain, models with stale training snapshots converge on the same wrong answer while agreement-based scoring reports high confidence (R00473); conformal guarantees break under continual domain pretraining (R00038). **Gap:** no study in the corpus measures how confidence and calibration on *financial* facts (rates, limits, rules, prices) degrade with the age of the fact relative to the training cut-off.

**G2 – Does *how* a fact was learned explain *how sure* the model is? (bridge A ↔ B)**
Overconfidence follows knowledge popularity (R00014); hallucination is bounded by the monofact rate minus miscalibration (R00002); verbalized confidence can be traced to training data (R00047); knowledge probes can be scored by calibration, not only accuracy (R00049). In finance, fine-tuning on domain content made a model more confident without matching gains (R00341), financial fine-tuning did not remove numerical hallucination (R00413), and SFT vs continued pretraining inject institutional knowledge differently (R00537). **Gap:** no controlled study varies the *acquisition route* of the same financial facts (pre-training frequency vs fine-tuning vs continued pretraining vs in-context) and measures the resulting calibration of token-level and verbalized confidence.

**G3 – Uncertainty for advice, not answers.**
UQ methods are validated on factual QA with one right answer; they degrade under ambiguity (R00039), conflate several uncertainty sources (R00066), and measure sample agreement rather than correctness (R00077, R00104). Financial advice has no single correct answer, and LLM advice already varies with irrelevant input changes (R00319), language/country (R00340) and model (R00333). **Gap:** no uncertainty measure separates legitimate variation in advice (different valid allocations) from model uncertainty, and none is validated on financial advice.

**G4 – Homogeneous models make agreement a false confidence signal.**
Aligned models give near-identical samples, which leaves sampling-based UQ with no signal (R00571); open-ended outputs are homogeneous within and across models (R00562); epistemic diversity is low (R00559, R00584) and model diversity protects against knowledge collapse (R00564); investment recommendations converge across LLMs (R00333) and multi-LLM consensus can confidently converge on a fabrication (R00473). **Gap:** consistency- and consensus-based confidence is widely used, but its validity for financial questions under cross-model homogeneity has not been tested.

**G5 – Expressed confidence in financial advice and how users respond.**
Verbalized overconfidence is systematic (R00003, R00063, R00118) and users follow confident LLMs (R00159, R00172, R00173, R00203, R00209), but these user studies use general-knowledge or science tasks. In finance, the evidence is about the model side only: conviction rises when an asset is named (R00475), confident errors in financial QA (R00407), decision value of confidence depends on the downstream rule (R00411). **Gap:** no study measures both the calibration of an LLM's expressed confidence in *financial advice* and the effect of that expression on retail users' decisions.

**G6 – Few finance benchmarks for calibration.**
Large UQ benchmarks are general-domain (R00016, R00037, R00079); finance has benchmark-validity and calibration work for statement verification (R00404) and calibration of predictions (R00431), but no time-stamped financial-knowledge benchmark scored on calibration. (Supports G1/G2 as a data contribution rather than a separate RQ.)

## Evidence set for full-text + citation check (38 papers)

G1: R00508, R00530, R00473, R00038, R00014 · G2: R00002, R00047, R00049, R00341, R00413, R00537 · G3: R00039, R00066, R00077, R00104, R00012, R00319, R00340, R00333 · G4: R00571, R00562, R00559 (seed), R00584, R00564 · G5: R00003, R00063, R00118, R00159, R00172, R00173, R00203, R00209, R00475, R00407, R00411 · G6: R00016, R00079, R00404.

Papers that fail the full-text or citation check are removed and the gap text is revised (runbook stop condition: a failed check that changes an RQ's evidence base → stop and ask Frank).
