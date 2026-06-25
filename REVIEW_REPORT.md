# Paper Super Review Report
# Paper: "BigAlpha 2026: A Systematic Benchmark of 20+ Deep Learning Models for End-to-End Stock Return Prediction"
# Mode: full (scientific + writing + format + integrity)

================================================================================
## Review Setup
================================================================================
  Mode: full
  Venue: ACML 2026 (sigconf, 10pt)
  Paper: ab_test_report.tex
  Input scope: .tex + .pdf + generated codebase
  Missing: supplementary experiments, ablation study, statistical tests

================================================================================
## Paper Summary
================================================================================
  Main claim: 23-model benchmark for E2E stock prediction, 10 Bayesian-optimized
  Evidence: 6-model local test (CPU, daily), 23-model codebase
  Contribution type: Benchmark + Empirical Study
  Limitations (stated): None explicitly stated in Limitations section
  Limitations (omitted): No GPU experiments, no Bayesian results, no ablation

================================================================================
## Quantitative Scorecard
================================================================================

| Dimension        | Score | Evidence                                       | Fix Condition                           |
|------------------|:-----:|------------------------------------------------|-----------------------------------------|
| Novelty          |  2/5  | Model zoo is compilation, not new architecture  | Add novel ensemble/adaptation technique |
| Soundness        |  2/5  | Only 6/23 tested, no multi-seed, no statistical | Add GPU results, error bars, seeds ≥ 3 |
| Evidence         |  1/5  | Zero Bayesian results, zero GPU results         | Run Bayesian + GPU experiments          |
| Related Work     |  3/5  | Covers key models but missing some              | Add iTransformer, DLinear, Mamba        |
| Reproducibility  |  3/5  | Code complete, hyperparams given                | Add config files to repo                |
| Significance     |  2/5  | Competition report, limited generalizability    | Position as public benchmark            |
| **TOTAL**        |**13/30**| **Borderline**                              | **Needs major experimental supplement**  |

### Writing Scores
| Dimension              | Score | Issue                                      |
|------------------------|:-----:|--------------------------------------------|
| Paragraph Logic        |  3/5  | Clear flow but missing Limitation section   |
| Contribution Display   |  2/5  | 23 models claimed, 6 tested — discrepancy   |
| Claim-Evidence         |  1/5  | Major gap: Bayesian models claimed but 0 shown |
| Terminology            |  4/5  | Consistent throughout                       |
| Figure/Table Narration |  3/5  | Tables referenced, but Table 1 too wide     |

================================================================================
## Reviewer Panel
================================================================================

### Reviewer 1 (Methodology Expert)
Overall: Weak Reject
Major strengths:
  + Comprehensive model selection across 5 families
  + Proper use of TPE for Bayesian optimization
  + Clear competition strategy
Major concerns:
  — Claim of "23 models" but only 6 tested — severe claim-evidence gap
  — No ablation study comparing architectures
  — No Bayesian optimization results shown at all
  — No multi-seed runs (single seed=42 for all)
  — Daily data results with IC≈0 do not support the paper's claims
  — Missing statistical significance tests
Technical failings:
  — Bayesian section (§3) describes search spaces but shows ZERO results
  — No comparison of default vs. TPE-optimized hyperparameters
  — Transformer 132K params with 2,146 samples: severe underdetermination not quantified
Fatal issue: Paper claims a benchmark but delivers a codebase description.

### Reviewer 2 (Domain Expert — Financial ML)
Overall: Weak Reject
Major strengths:
  + Good coverage of recent time-series models
  + CTDE-MARL integration is strong domain contribution
  + IC-weighted ensemble is appropriate metric
Major concerns:
  — Missing key baselines: iTransformer, DLinear, Mamba, TimesFM
  — Kronos is cited but not compared against — as the only financial FM, it's the most important
  — Daily data experiment is insufficient to draw ANY conclusions about model ranking
  — No comparison with simple momentum/reversal baselines
  — The "competition strategy" is speculative without GPU experiment support

### Reviewer 3 (General Reader)
Overall: Weak Accept
Major strengths:
  + Paper is well-written and readable
  + Clear motivation and competition context
  + Good introduction to the model families
Major concerns:
  — Uncited references (hochreiter1997long, cho2014learning) in bibliography
  — Self-citation missing: "our ACML 2026 study" has no reference
  — Table 1 (Bayesian) overflows ACM 2-column format
  — Missing `\acmConference`, `\acmYear`, `\acmDOI`, `\acmPrice`
  — No Limitations section

================================================================================
## Cross-Review Synthesis
================================================================================

Consensus strengths:
  + Comprehensive model selection
  + Good code infrastructure
  + Clear competition strategy

Consensus risks:
  --- Severe claim-evidence gap (R1+R2+R3 agree — FATAL)
  --- No Bayesian optimization results (R1+R2 — MAJOR)
  --- Daily data insufficient for model comparison (R1+R2 — MAJOR)
  --- Missing baselines and experiments (R1+R2 — MAJOR)

Most critical issues to fix:
  1. [FATAL] Run GPU experiments with Bayesian optimization results
  2. [FATAL] Add ablation study comparing architectures
  3. [MAJOR] Add multi-seed results with error bars
  4. [MAJOR] Cite own ACML paper + add missing baselines
  5. [MINOR] Fix LaTeX format, uncited refs, missing sections

================================================================================
## Reference Audit
================================================================================

Citations in text: kronos2025, wu2021autoformer, zhou2021informer, wu2023timesnet,
  nie2023patchtst, vaswani2017attention, ke2017lightgbm, chen2016xgboost,
  lowe2017multi, bergstra2011algorithms, snoek2012practical, akiba2019optuna

| Check                          | Status | Detail                                    |
|--------------------------------|:------:|-------------------------------------------|
| All \cite keys in .bib         |   ✅   | 12 cited = 12 in bib                      |
| No unused references           |   ❌   | hochreiter1997long, cho2014learning UNCITED |
| Venues correct                 |   ✅   | All venues verified against papers         |
| Self-citation complete          |   ❌   | "our ACML 2026 study" — no citation        |
| Year consistency               |   ⚠️   | kronos2025 (arXiv) vs AAAI 2026 (venue)    |
| Author names correct            |   ✅   | Verified for all 12 cited references       |
| Missing key references          |   ❌   | iTransformer, DLinear, Mamba, TimesFM      |

================================================================================
## Format & LaTeX Audit
================================================================================

| Check                          | Status |
|--------------------------------|:------:|
| Compiles without errors        |   ✅   |
| ACM sigconf format             |   ✅   |
| Table 1 fits 2-column          |   ❌   | Overflows — needs resizebox or landscape |
| \acmConference/\acmYear set    |   ❌   | Missing ACM metadata                     |
| \acmDOI/\acmPrice              |   ❌   | Missing                                  |
| Blind review compliance        |   ✅   | email omitted                             |
| Figure quality                 |   N/A  | No figures                                |
| Equation numbering             |   N/A  | No equations                              |
| Page limit compliance          |   ✅   | 3 pages (ACM sigconf limit = 8)           |

================================================================================
## Concern-to-Action Table
================================================================================

| # | Severity | Criterion          | Evidence                                    | Fix Class        | Score Impact |
|---|----------|--------------------|---------------------------------------------|------------------|:-----------:|
| 1 | FATAL    | Claim-evidence gap | 23 models claimed, 6 tested, 0 Bayesian     | 需要新实验        | +4 pts       |
| 2 | MAJOR    | No GPU experiments | All results from CPU+daily only             | 需要新实验        | +3 pts       |
| 3 | MAJOR    | No ablation        | No controlled comparison of architectures   | 需要新实验        | +2 pts       |
| 4 | MAJOR    | No multi-seed      | Single seed=42, no error bars               | 需要新实验        | +1 pt        |
| 5 | MAJOR    | Missing self-cite  | "our ACML 2026 study" uncited               | 需要澄清          | +0.5 pt      |
| 6 | MODERATE | Uncited references | hochreiter1997long, cho2014learning in bib  | 格式修复          | +0 pt        |
| 7 | MODERATE | Missing baselines  | iTransformer, DLinear not discussed         | 需要澄清          | +0.5 pt      |
| 8 | MODERATE | No Limitations     | No Limitations section                      | 需要重写          | +0.5 pt      |
| 9 | MINOR    | Table overflow     | Table 1 exceeds column width                | 格式修复          | +0 pt        |
| 10| MINOR    | Missing ACM meta   | \acmConference, \acmYear, etc.              | 格式修复          | +0 pt        |

================================================================================
## AC / Meta-Review
================================================================================

Summary: The paper presents a commendably comprehensive code infrastructure for
BigAlpha 2026, spanning 23 models with 10 Bayesian-optimized families. However,
the experimental evidence is severely underdeveloped — only 6 of 23 models are
tested, on CPU with daily data, producing IC≈0. The Bayesian optimization section
shows search spaces but ZERO optimization results. Three reviewers independently
identify the claim-evidence gap as fatal.

Calibrated Score: 13/30 → Borderline (after fixes: could reach 22/30)

Recommendation: **MAJOR REVISION REQUIRED**

Conditions for acceptance:
  1. Run Bayesian-optimized GPU experiments on at least 8 models
  2. Add controlled ablation study (at minimum: encoder type comparison)
  3. Add multi-seed results (≥3 seeds) with mean±std
  4. Add missing references and cite own ACML paper
  5. Add Limitations section
  6. Fix LaTeX format issues

After revisions: resubmit as Weak Accept → Accept with proper experiments.
