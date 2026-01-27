# Benchmarking RNA Tertiary Structure Prediction Models and Evaluation Metrics

This repository contains code and example data accompanying:

> **Benchmarking RNA tertiary structure prediction models and evaluation metrics**  
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
![Overview](src/overview.jpg)
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

A suggested structure:

```text
.
├── datasets
│   ├── dataset1
│   ├── dataset2
│   └── dataset3
├── demo
│   ├── fold_sars_model_0.cif
│   ├── fold_sars_model_0.fixed.pdb
│   └── fold_sars_model_0.pdb
├── figures
│   ├── dataset3_radar_deep_learning.pdf
│   ├── dataset3_radar_energy_metrics.pdf
│   ├── dataset3_radar_plot_energy_metrics.pdf
│   ├── dataset_resolution_distribution.pdf
│   ├── dataset_sequence_length_distribution.pdf
│   ├── dendrogram_plot_of_RNA_tertiary_structure_evaluation_metrics.pdf
│   ├── dendrogram_plot_of_RNA_tertiary_structure_evaluation_metrics.png
│   ├── method_legend.pdf
│   ├── metrics_correlation_GC.pdf
│   ├── metrics_correlation_pair_ratio.pdf
│   ├── metrics_correlation_with_sequence_length.pdf
│   ├── PCA_plot_of_RNA_tertiary_structure_evaluation_metrics.pdf
│   ├── performance_evaluation_on_dataset1_3drnascore.pdf
│   ├── performance_evaluation_on_dataset1_ARES.pdf
│   ├── performance_evaluation_on_dataset1_BARNABA-eSCORE.pdf
│   ├── performance_evaluation_on_dataset1_cgRNASP.pdf
│   ├── performance_evaluation_on_dataset1_clash.pdf
│   ├── performance_evaluation_on_dataset1_DFIRE.pdf
│   ├── performance_evaluation_on_dataset1_f1.pdf
│   ├── performance_evaluation_on_dataset1_GDT-TS.pdf
│   ├── performance_evaluation_on_dataset1_INF-ALL.pdf
│   ├── performance_evaluation_on_dataset1_lddt.pdf
│   ├── performance_evaluation_on_dataset1_LociPARSE.pdf
│   ├── performance_evaluation_on_dataset1_PAMnet.pdf
│   ├── performance_evaluation_on_dataset1_precision.pdf
│   ├── performance_evaluation_on_dataset1_RASP-ENERGY.pdf
│   ├── performance_evaluation_on_dataset1_recall.pdf
│   ├── performance_evaluation_on_dataset1_RMSD.pdf
│   ├── performance_evaluation_on_dataset1_RNA3DCNN.pdf
│   ├── performance_evaluation_on_dataset1_RNA-BRiQ.pdf
│   ├── performance_evaluation_on_dataset1_RNArank.pdf
│   ├── performance_evaluation_on_dataset1_tb_mcq.pdf
│   ├── performance_evaluation_on_dataset1_TM-score.pdf
│   ├── performance_evaluation_on_dataset2_3drnascore.pdf
│   ├── performance_evaluation_on_dataset2_ARES.pdf
│   ├── performance_evaluation_on_dataset2_BARNABA-eSCORE.pdf
│   ├── performance_evaluation_on_dataset2_cgRNASP.pdf
│   ├── performance_evaluation_on_dataset2_clash.pdf
│   ├── performance_evaluation_on_dataset2_DFIRE.pdf
│   ├── performance_evaluation_on_dataset2_f1.pdf
│   ├── performance_evaluation_on_dataset2_GDT-TS.pdf
│   ├── performance_evaluation_on_dataset2_INF-ALL.pdf
│   ├── performance_evaluation_on_dataset2_lddt.pdf
│   ├── performance_evaluation_on_dataset2_LociPARSE.pdf
│   ├── performance_evaluation_on_dataset2_PAMnet.pdf
│   ├── performance_evaluation_on_dataset2_precision.pdf
│   ├── performance_evaluation_on_dataset2_RASP-ENERGY.pdf
│   ├── performance_evaluation_on_dataset2_recall.pdf
│   ├── performance_evaluation_on_dataset2_RMSD.pdf
│   ├── performance_evaluation_on_dataset2_RNA-BRiQ.pdf
│   ├── performance_evaluation_on_dataset2_RNArank.pdf
│   ├── performance_evaluation_on_dataset2_tb_mcq.pdf
│   ├── performance_evaluation_on_dataset2_TM-score.pdf
│   ├── ROC_deep_learning_metrics_LDDT_as_label.pdf
│   ├── ROC_deep_learning_metrics_RMSD_as_label.pdf
│   ├── ROC_deep_learning_metrics_TM_score_as_label.pdf
│   ├── ROC_energy_metrics_LDDT_as_label.pdf
│   ├── ROC_energy_metrics_RMSD_as_label.pdf
│   └── ROC_energy_metrics_TM_score_as_label.pdf
├── metrics
│   ├── ARES
│   ├── Clash
│   ├── PAMNet
│   ├── Precision_Recall_F1
│   ├── RNA3DCNN
│   ├── rnadvisor
│   └── RNArank
├── models
│   ├── 3dRNAv2.0
│   ├── Alphafold3
│   ├── DeepoFoldRNA
│   ├── DRfold
│   ├── DRfold2
│   ├── FARFAR2
│   ├── NuFold
│   ├── RhoFold
│   ├── RNAComposer
│   ├── RNAJP
│   ├── RoseTTAFold2NA
│   ├── SimRNA
│   ├── trRosettaRNA
│   └── Vfold
├── README.md
├── results
│   ├── dataset1
│   ├── dataset2
│   ├── dataset3
│   ├── dataset_statistics
│   └── metrics
├── scripts
│   ├── data_prepare.ipynb
│   ├── dataset_statistics.ipynb
│   ├── metrics_correlation_with_GC_content.ipynb
│   ├── metrics_correlation_with_pairing_ratio.ipynb
│   ├── metrics_correlation_with_sequence_length.ipynb
│   ├── metrics_PCA_and_clustering_analysis.ipynb
│   ├── performance_evaluation_on_dataset1.ipynb
│   ├── performance_evaluation_on_dataset2.ipynb
│   ├── performance_evaluation_on_dataset3.ipynb
│   ├── __pycache__
│   ├── ROC_of_deep_learning_metrics.ipynb
│   ├── ROC_of_energy_metrics.ipynb
│   └── utils.py
└── src
    └── Overview.jpg


```

---
## 3. Data

### 3.1 Datasets Overview

We constructed **three curated RNA structure datasets** with distinct design principles to provide comprehensive and unbiased evaluation:

| Dataset | Design Purpose | Size | Length Range | Source | Key Features |
|---------|----------------|------|--------------|--------|--------------|
| **Dataset1** | Standard benchmark for well-folded RNAs | 17 RNAs | 37-134 nt | CASP16 & RNA-Puzzles | High-resolution (1.55-3.04 Å) canonical structures |
| **Dataset2** | Temporal hold-out test for generalization | 16 RNAs | 17-277 nt | Post-publication structures | Strictly post-dates model publication dates |
| **Dataset3** | Reference-free ab initio evaluation | 17 RNAs | - | Human/mouse transcriptome | No experimental 3D structures available |

### 3.2 Dataset Details

#### **Dataset1: High-Resolution Canonical RNAs**
- **Source**: CASP16 competition and RNA-Puzzles initiative
- **Selection criteria**: 
  - Experimentally resolved, well-folded RNAs
  - High-quality reference structures (1.55-3.04 Å resolution)
  - Diverse structural classes including viral elements, ribozymes, and tRNAs
- **Purpose**: Standard benchmark representing the "gold standard" in RNA structural biology

#### **Dataset2: Temporal Hold-Out RNAs**
- **Construction principle**: All structures were released **strictly after** the publication date of each corresponding prediction model
- **Data leakage prevention**: Ensures models cannot have been trained on these structures
- **Structural diversity**: Includes RNAs with varying resolution (2.4-8.57 Å) and complexity
- **Purpose**: Unbiased test of model generalization capability to novel RNA folds

#### **Dataset3: Reference-Free Ab Initio RNAs**
- **Source**: Human and mouse transcriptomes
- **Selection methodology**: Multi-criteria filtering to enrich for stable tertiary folds:
  1. **icSHAPE reactivity profiles** – identifies structured regions
  2. **ENTRNA foldability scores** – predicts RNA foldability
  3. **RNAfold energy predictions** – estimates thermodynamic stability
- **Unique feature**: No experimentally determined 3D structures exist for any RNA in this dataset
- **Purpose**: Evaluation of prediction methods and scoring functions in purely ab initio contexts


---
## 4. RNA 3D Structure Prediction Models

### 4.1 Overview of Evaluated Methods

We benchmarked **14 representative RNA tertiary structure prediction models** spanning three major methodological categories:

| Category | Models Included | Core Methodology | Key Features |
|----------|-----------------|------------------|--------------|
| **Statistical Potential & Ab Initio** | SimRNA, RNAJP | Coarse-grained sampling, fragment assembly, statistical potentials | Physics-inspired, template-free conformational exploration |
| **Template/Fragment-Driven** | RNAComposer, 3dRNA v2.0, FARFAR2, VFold | Structural database integration, MSA coevolution, fragment libraries | Knowledge-guided construction using evolutionary signals |
| **Deep Learning-Based** | DRfold, DRfold2, RhoFold, RoseTTAFold2NA, trRosettaRNA, DeepFoldRNA, AlphaFold3, NuFold | RNA transformers, cross-modal architectures, EvoFormer modules | Neural network prediction of complex long-range interactions |

### 4.2 Model Details

#### **4.2.1 Statistical Potential & Ab Initio Methods**
- **[SimRNA](https://genesilico.pl/SimRNAweb/)** – Coarse-grained Monte Carlo sampling with statistical potential for template-free conformational exploration.
- **[RNAJP](http://rna.physics.missouri.edu/vfold_software_download/RNAJP_download.html)** – Junction-based modeling approach employing fragment libraries for RNA 3D structure prediction.

#### **4.2.2 Template & Fragment-Driven Methods**
- **[RNAComposer](https://rnacomposer.cs.put.poznan.pl)** – Template-based modeling system utilizing the RNA FRABASE database for automated structure construction.
- **[3dRNA v2.0](http://biophy.hust.edu.cn/new/3dRNA)** – Fragment assembly approach with knowledge-based scoring function for RNA structure prediction.
- **[FARFAR2](https://github.com/RosettaCommons/rosetta.git)** – Fragment assembly of RNA using the Rosetta energy function and conformational sampling.
- **[VFold](https://rna.physics.missouri.edu/vfoldPipeline/)** – V-fold model combining statistical potentials and fragment libraries for 3D structure prediction.

#### **4.2.3 Deep Learning-Based Methods**
- **[trRosettaRNA](https://yanglab.qd.sdu.edu.cn/trRosettaRNA/)** – Integrates deep learning-predicted distance/orientation restraints with fragment assembly for structure generation.
- **[DRfold](https://github.com/leeyang/DRfold.git)** – End-to-end deep learning framework with hybrid energy network for direct RNA structure prediction.
- **[DRfold2](https://github.com/leeyang/DRfold2.git)** – DRfold2 is a deep learning method for RNA structure prediction. At its core, DRfold2 utilizes the RNA Composite Language Model (RCLM), which provides enhanced full likelihood approximation capabilities to effectively capture co-evolutionary signals from unsupervised sequence data.
- **[RhoFold](https://github.com/ml4bio/RhoFold.git)** – RNA transformer architecture incorporating geometric constraints for accurate structure modeling.
- **[RoseTTAFold2NA](https://github.com/uw-ipd/RoseTTAFold2NA.git)** – Three-track neural network architecture specifically designed for nucleic acid structure prediction.
- **[DeepFoldRNA](https://github.com/robpearc/DeepFoldRNA.git)** – Comprehensive deep learning framework for RNA tertiary structure prediction from sequence.
- **[AlphaFold3](https://alphafoldserver.com/)** – Generalized architecture for biomolecular structure prediction, including RNA modeling capabilities.
- **[NuFold](https://github.com/kiharalab/NuFold.git)** – NuFold is a state-of-the-art method designed for predicting 3D RNA structures, leveraging deep learning for high accuracy and reliability. This tool is particularly useful for biologists and bioinformatics researchers focusing on RNA function and structure. 

---
## 5. Evaluation Metrics

### 5.1 Overview of Evaluation Framework

We employed **21 complementary metrics** spanning four major methodological categories:

| Category | Metrics Included | Evaluation Focus | Key Characteristics |
|----------|-----------------|------------------|---------------------|
| **Geometry-Based** | RMSD, TM-score, lDDT, GDT-TS, Clash score, BARBABA-eSCORE | Atomic coordinate similarity | Quantify global and local structural deviations |
| **Topology-Based** | INF, Base-pair F1 score, Precision, Recall | Base-pairing pattern correctness | Assess secondary structure and contact map accuracy |
| **Energy-Based** | RASP, cgRNASP, 3dRNAscore, RNA-BRIQ, DFIRE | Structural plausibility and stability | Statistical/knowledge-based potentials from experimental structures |
| **Deep Learning-Based** | ARES, LociPARSE, RNARank, RNA3DCNN, TB-MCQ, PAMNet | Neural network discrimination | Learned representations for native vs. decoy classification |

### 5.2 Metric Details

#### **5.2.1 Geometry-Based Metrics**
- **RMSD/[TM-score](https://aideepmed.com/TM-score/)/lDDT/GDT-TS** – Standard structural similarity measures including Root Mean Square Deviation, Template Modeling score, local Distance Difference Test, and Global Distance Test.
- **Clash score** – Evaluates structural plausibility by counting steric clashes in predicted models.
- **BARBABA-eSCORE** – Ensemble-based scoring method for assessing RNA structure quality and native-likeness.

#### **5.2.2 Topology-Based Metrics**
- **INF** – Interaction Network Fidelity metric measuring correctness of predicted base-pair interactions and contact maps.
- **Base-pair F1 score/Precision/Recall** – Standard classification metrics for evaluating base-pair prediction accuracy using tools like RNAView and MC-Annotate.

#### **5.2.3 Energy-Based Metrics**
- **RASP** – RNA Assessment of Structures Package providing knowledge-based potentials for RNA structure evaluation.
- **cgRNASP** – Coarse-grained statistical potential specifically designed for RNA structure assessment.
- **3dRNAscore** – Scoring function optimized for RNA tertiary structures incorporating multiple structural features.
- **RNA-BRIQ** – Bayesian model for RNA structure quality assessment using reference-free evaluation principles.
- **DFIRE** – Distance-scaled Finite Ideal-gas Reference potential for statistical evaluation of RNA structures.

#### **5.2.4 Deep Learning-Based Metrics**
- **[ARES](http://drorlab.stanford.edu/ares.html)** – Atomic Rotationally Equivariant Scorer employing geometric deep learning for RNA structure assessment.
- **[RNArank](https://github.com/YangLab-SDU/RNArank.git)** – Neural network framework for ranking RNA structural models based on quality predictions.
- **[RNA3DCNN](https://github.com/lijunRNA/RNA3DCNN.git)** – 3D convolutional neural network architecture for comprehensive RNA structure assessment.
- **[TB-MCQ](https://github.com/EvryRNA/RNA-TorsionBERT)** – Template-based Model Quality Assessment method leveraging structural similarities for scoring.
- **[PAMNet](https://github.com/XieResearchGroup/Physics-aware-Multiplex-GNN.git)** – Point Attention Network for RNA structure evaluation using attention mechanisms on point cloud representations.
- **[LociPARSE](https://github.com/Bhattacharya-Lab/lociPARSE.git)** – lociPARSE is a locality-aware invariant point attention–based scoring function that predicts RNA 3D structure accuracy using superposition-free lDDT, enabling more reliable model evaluation and scoring-guided conformational sampling.


