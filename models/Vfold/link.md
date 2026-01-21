# Vfold Pipeline

## Overview

**Vfold Pipeline** is a fully automated framework for **RNA three-dimensional (3D) structure prediction directly from RNA sequences**.  
Developed by the **Chen Group**, the Vfold Pipeline integrates RNA secondary structure prediction with tertiary structure modeling, providing an end-to-end solution for RNA 3D structure prediction.

The pipeline first predicts RNA secondary (2D) structures using **Vfold2D**, and then constructs RNA 3D structures based on the predicted 2D structures using **Vfold3D** and **VfoldLA**.

---

## Method Description

The Vfold Pipeline consists of two main stages:

1. **Secondary Structure Prediction (Vfold2D)**  
   RNA secondary structures are predicted from the input sequence, with optional inclusion of **H-type pseudoknots** and **SHAPE experimental restraints**.

2. **Tertiary Structure Prediction (Vfold3D / VfoldLA)**  
   RNA 3D structures are assembled based on the predicted secondary structures using:
   - **A-form helices**
   - **Loop and motif templates** extracted from known RNA 3D structures

This assembly-based strategy enables efficient modeling of RNA tertiary structures from sequence information alone.

---

## Limitations

Due to the current size and coverage of the template library, **Vfold Pipeline may not generate predictions for some RNA targets** when suitable templates are unavailable.

---

## Web Server and Software

- **Vfold Pipeline Web Server**  
  Available through the [Chen Group website](https://rna.physics.missouri.edu/vfoldPipeline/)

- **Standalone Vfold Pipeline Package**  
  The standalone version can be downloaded by submitting a request form at:  
  [VfoldPipeline_standalone](http://rna.physics.missouri.edu/vfold_software_download/vfoldpipeline_download.html)

- **Documentation**
  - [Supplementary-Information.pdf](https://rna.physics.missouri.edu/vfoldPipeline/Supplementary-Information.pdf)
  - [VfoldPipeline-standalone-manual.pdf](https://rna.physics.missouri.edu/vfoldPipeline/VfoldPipeline-standalone-manual.pdf)

---

## Input Options

The Vfold Pipeline web server supports flexible input configurations:

1. **RNA Sequence**  
   - Single-stranded RNA only  
   - Maximum length: **300 nucleotides**  
   - Accepted characters: `A U G C a u g c`

2. **Secondary Structure (Optional)**  
   - Dot-bracket notation  
   - Accepted symbols: `.()[]<>{}`  
   - If not provided, secondary structure is predicted by **Vfold2D**

3. **Maximum Number of Predicted 2D Structures**  
   - User-defined number of secondary structures used for 3D prediction

4. **Pseudoknot Option**  
   - Optional inclusion of **H-type pseudoknots**

5. **Temperature**  
   - Temperature for secondary structure prediction (default: 37 °C)

6. **SHAPE Restraints (Optional)**  
   - SHAPE probing data can be uploaded to guide secondary structure prediction

7. **Excluded Templates (Optional)**  
   - User-specified PDB IDs to exclude from the template library

8. **Job Name and Email Notification (Optional)**  
   - Results can be sent via email (Gmail not supported)

---

## Example Workflows

- **Example 1**  
  Predicts secondary structures *without* H-type pseudoknots and generates 3D structures for **tRNA 1ffy**.

- **Example 2**  
  Predicts secondary structures *with* H-type pseudoknots using **SHAPE restraints**, followed by 3D structure prediction for **RNA 1e95**.

- **Example 3**  
  Predicts 3D structures for **RNA 1e95** using a **user-provided secondary structure**.

---

## Key Features

- Fully automated RNA 3D structure prediction from sequence
- Integrated secondary and tertiary structure modeling
- Support for H-type pseudoknots
- Incorporation of SHAPE experimental data
- Template-based assembly using known RNA 3D motifs
- Web server and standalone package available

---

## Usage Notes

- Prediction accuracy strongly depends on the quality of secondary structure prediction.
- SHAPE restraints can significantly improve secondary and tertiary structure modeling.
- The pipeline is optimized for RNAs up to **300 nucleotides**.

---

## Citation

If you use **Vfold Pipeline** in your research, please cite:

```bibtex
@article{li2022vfoldpipeline,
  title={Vfold-Pipeline: a web server for RNA 3D structure prediction from sequences},
  author={Li, J. and Zhang, S. and Zhang, D. and Chen, Shi-Jie},
  journal={Bioinformatics},
  volume={38},
  number={16},
  pages={4042--4043},
  year={2022},
  doi={10.1093/bioinformatics/btac512}
}
