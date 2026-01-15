# Benchmarking RNA Tertiary Structure Prediction Models and Evaluation Metrics

This repository contains code and example data accompanying:

> **Benchmarking RNA tertiary structure prediction models and evaluation metrics**  
> You Wu, Xiang Li, Dongke Zhou, Pengfei Xu, Xiang Yu  
> (manuscript)

We provide a **reproducible pipeline** for:
- processing RNA 3D structures into benchmark-ready datasets,
- running **14 publicly available RNA tertiary structure prediction methods**, and
- evaluating predictions using **21 complementary structural metrics**  
  (geometry, topology, energy-based, and deep-learning–based scores),

as well as scripts to reproduce the **main figures** in the manuscript.

---

## 1. Overview

The goal of this project is to offer a **transparent, reproducible benchmark** of modern RNA 3D structure prediction tools and evaluation metrics.

We:
- Construct **three curated datasets**:
  - **Dataset1** – 17 high-resolution RNAs from CASP16 & RNA-Puzzles  
  - **Dataset2** – 16 **temporally independent** RNAs (post-publication hold-out)  
  - **Dataset3** – 17 **reference-free** human/mouse RNAs enriched for stable tertiary folds
- Benchmark **14 prediction methods** spanning:
  - statistical potential–based / ab initio,
  - template / fragment-driven, and
  - deep learning–based models.
- Evaluate predictions using **21 metrics**, grouped into:
  - geometry-based,
  - topology-based,
  - energy-based, and
  - deep learning–based evaluation metrics.
- Provide **plotting scripts** to reproduce figures (e.g. performance violin plots, radar plots, PCA/clustering of metrics, ROC curves).

This repository hosts:
- **Data preprocessing scripts**  
- **Example benchmark data**  
- **Plotting code** for Figures 1–7

---

## 2. Repository structure

A suggested structure (adjust to match your repo):

```text
.
├── data/
│   ├── dataset1/                  # Processed structures / metadata for Dataset1
│   ├── dataset2/                  # Processed structures / metadata for Dataset2
│   ├── dataset3/                  # Processed sequences & filters for Dataset3
│   ├── metrics/                   # Precomputed metric tables (CSV/TSV)
│   └── examples/                  # Small example subset for quick tests
├── scripts/
│   ├── 01_preprocess_structures.py
│   ├── 02_run_predictors.sh       # Example wrapper to run external methods
│   ├── 03_compute_metrics.py      # Calls RNAdvisor / RNA_assessment / etc.
│   └── utils/                     # Helper functions (I/O, plotting helpers…)
├── plot/
│   ├── figure1_overview.R
│   ├── figure2_model_performance.R
│   ├── figure3_temporal_holdout.R
│   ├── figure4_reference_free.R
│   ├── figure5_sequence_factors.R
│   ├── figure6_metric_PCA_clustering.R
│   └── figure7_metric_comparison_ROC.R
├── env/
│   ├── environment.yml            # Conda env for Python tools (optional)
│   └── renv/ or requirements_R.txt  # R package environment (optional)
└── README.md

## 3. Data

3.1 Datasets
dataset1
dataset2
dataset3

## 4. Models

## 5. Metrics




