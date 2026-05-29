# LockGuard RL-X

**Adversarial Irreversibility Governance for Multi-Agent Financial Systems**

Un framework de gobernanza en tiempo real para detectar y contener irreversibilidad adversarial en entornos MARL financieros.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20436834.svg)](https://doi.org/10.5281/zenodo.20436834)

## 🎯 Descripción

LockGuard RL-X es una **capa de gobernanza** que supervisa sistemas multi-agente de trading, detecta coordinación adversarial y aplica intervenciones graduadas antes de que se produzcan cascadas irreversibles (flash crashes, liquidaciones en cadena, etc.).

Forma parte del framework más amplio **LockGuard**, que une psicología organizacional, optimización estratégica y gobernanza técnica adversarial.

## ✨ Componentes Principales

- **AII** — Adversarial Irreversibility Index
- **GΨ** — Coalition Graph (detección de coaliciones)
- **A-CIM** — Adversarial Causal Intervention Matrix
- **EGDS-X** — Execution-Gated Decision System (4 niveles)
- **BGE** — Bounded Governance Escalation

## 📊 Resultados Principales

- Reducción de eventos catastróficos: **64–78%**
- Detección de coaliciones: F1 ≈ **0.80**
- Reducción de máximo drawdown: **hasta 73%**
- Overhead de rendimiento: **8–14%**

## 📄 Paper

**LockGuard RL-X: A Governance Runtime for Real-Time Detection and Containment of Adversarial Irreversibility in Multi-Agent Financial Systems**

- [📥 Descargar PDF completo](paper/LockGuard_RL-X_Paper.pdf)
- DOI: [10.5281/zenodo.20436834](https://doi.org/10.5281/zenodo.20436834)

## 🚀 Cómo ejecutar

```bash
# Clonar repositorio
git clone https://github.com/uberlandisfiolreyes74-spec/lockguard-rl-x.git
cd lockguard-rl-x

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar benchmark
python scripts/run_benchmark.py
