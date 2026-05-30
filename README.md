# LockGuard RL-X: Governance Runtime for Adversarial Irreversibility in Multi-Agent Financial Systems

**Author:** Uberlandis Fiol Reyes  
**Affiliation:** LockGuard AI, Inc. | Independent Researcher  
**Contact:** [uberlandisfiolreyes74@gmail.com](mailto:uberlandisfiolreyes74@gmail.com)  
**License:** CC BY 4.0  
**DOI:** [10.5281/zenodo.20436834](https://doi.org/10.5281/zenodo.20436834)  

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20436834.svg)](https://doi.org/10.5281/zenodo.20436834)

---

## Overview

LockGuard RL-X is a **formally specified governance runtime** for real‑time detection and containment of **adversarial collective irreversibility** in multi‑agent reinforcement learning (MARL) systems, validated on FinRL financial trading benchmarks.

The architecture integrates five tightly coupled mechanisms:

1. **Adversarial Irreversibility Index (AII)** – a trajectory‑level metric quantifying the probability of catastrophic convergence.  
2. **Adversarial Causal Intervention Matrix (A‑CIM)** – a structured causal model tracking deceptive inter‑agent influence.  
3. **Coalition Graph (GΨ)** – detects synchronized agent behavior indicative of coordinated risk amplification.  
4. **EGDS‑X** – an execution‑gated decision system providing multi‑level intervention (ALLOW, CHECKPOINT, HALT, CONTAINMENT).  
5. **Bounded Governance Escalation (BGE)** – constrains intervention authority to prevent over‑governance.

Empirical results on FinRL environments show a **64–78% reduction in catastrophic drawdown events** over unconstrained MARL baselines, with only **8–14% mean performance overhead**, and **byte‑for‑byte reproducibility**.

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/lockguard-ai/lockguard-rlx.git
cd lockguard-rlx
