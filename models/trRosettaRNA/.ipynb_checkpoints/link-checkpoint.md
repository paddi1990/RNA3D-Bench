# trRosettaRNA

## Overview

**trRosettaRNA** is a deep learning–based method for **automated RNA three-dimensional (3D) structure prediction**.  
It employs a **transformer neural network** to predict both **inter-nucleotide geometries** and **RNA tertiary structures**, enabling accurate end-to-end RNA 3D modeling from sequence or multiple sequence alignment (MSA).

Blind benchmark evaluations, including **CASP15**, **CASP16**, and **RNA-Puzzles**, demonstrate that trRosettaRNA achieves performance **competitive with leading human expert teams**. The method has also been applied to generate confident structural models for **467 Rfam families** lacking experimentally determined structures.

The trRosettaRNA server is **freely accessible to all users**, including **commercial users**.

---

## Web Server and Software

- **trRosettaRNA Web Server**  
  [https://yanglab.qd.sdu.edu.cn/trRosettaRNA/](https://yanglab.qd.sdu.edu.cn/trRosettaRNA/)

- **Standalone Package and Source Code (Zenodo)**  
  Wenkai, W. *et al.*  
  *Source code and data for “trRosettaRNA: automated prediction of RNA 3D structure with transformer network”*  
  Zenodo (2023)  
  [https://zenodo.org/doi/10.5281/zenodo.8362613](https://zenodo.org/doi/10.5281/zenodo.8362613)

---

## Method Description

trRosettaRNA uses a **transformer-based deep learning architecture** to predict:

- Inter-nucleotide **contacts and distances**
- Relative **orientational geometries**
- RNA **secondary structure**
- Full RNA **3D atomic models**

If the initially generated 3D structure is not physically plausible, **Rosetta energy minimization** is applied to refine the model, guided by restraints derived from the predicted inter-nucleotide geometries. This hybrid deep learning and physics-based refinement strategy improves structural realism and stability.

---

## Output Results

The trRosettaRNA server provides comprehensive prediction outputs, including:

- **Predicted 3D structure model**  
  - Annotated with **global (molecule-wise)** and **local (nucleotide-wise)** confidence scores (**pLDDT**)

- **Predicted inter-nucleotide contacts and distances**

- **Predicted RNA secondary structure**

- **Multiple sequence alignment (MSA)** used for prediction

---

## Input Options

### Mandatory Input

Users must provide one of the following:

- **Single RNA sequence**
- **Multiple sequence alignment (MSA)**

Inputs can be pasted directly or uploaded as files.

### Optional Settings

- **Input type selection**: Single sequence or MSA
- **E-value cutoff** for homologous sequence search (default: 10)
- **Custom secondary structure input**
- **Target name** (user-defined identifier)
- **Email notification** (optional)
- **Private job option**  
  - Assigns a unique access key to keep results private

---

## Key Features

- Transformer-based deep learning for RNA 3D prediction
- Joint prediction of secondary structure, contacts, and 3D geometry
- Rosetta-based energy minimization with geometric restraints
- Confidence estimation using **pLDDT**
- Supports both single-sequence and MSA-based prediction
- Applicable to large-scale RNA structure annotation

---

## Recent Updates and News

- **03/25/2025** – Featured in *Nature Technology*: *RNA function follows form – why is it so hard to predict?*
- **12/01/2024** – Ranked **4th overall (1st among servers)** in CASP16 RNA prediction
- **11/01/2024** – Improved with a new end-to-end network and enhanced visualization
- **02/03/2024** – Standalone package updated to support custom secondary structures
- **10/13/2023** – trRosettaRNA paper accepted by *Nature Communications*
- **10/25/2022** – trRosettaRNA server officially launched

---

## Usage Notes

- MSA-based inputs generally yield higher prediction accuracy.
- Confidence scores (pLDDT) provide guidance for model reliability.
- Rosetta refinement improves physical plausibility of predicted structures.
- Suitable for **benchmarking, functional inference, and large-scale RNA annotation**.

---

## Citation

If you use **trRosettaRNA** in your research, please cite the following publications:

```bibtex
@article{wang2023trrosettarna,
  title={trRosettaRNA: automated prediction of RNA 3D structure with transformer network},
  author={Wang, Wenkai and others},
  journal={Nature Communications},
  volume={14},
  pages={7266},
  year={2023},
  doi={10.1038/s41467-023-42656-4}
}

@article{wang2026trrosettarna_protocols,
  title={The trRosettaRNA server for RNA structure prediction},
  author={Wang, Wenkai and others},
  journal={Nature Protocols},
  year={2026},
  note={in press}
}
