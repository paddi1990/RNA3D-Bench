# RNAComposer

## Overview

**RNAComposer** is a fully automated RNA three-dimensional (3D) structure modeling web server for predicting **large RNA tertiary structures**.  
It provides a user-friendly framework for RNA 3D structure prediction based on the **machine translation principle**, using the **RNA FRABASE database** as a dictionary that links RNA secondary structure elements to corresponding tertiary structure motifs.

Welcome to RNAComposer, a fully automated RNA structure modeling server.  
(Mirror site: rnacomposer.ibch.poznan.pl)

---

## Web Server

- **RNAComposer Web Server**  
  [https://rnacomposer.cs.put.poznan.pl/](https://rnacomposer.cs.put.poznan.pl/)

---

## Method Description

The RNAComposer system offers a novel approach to the **fully automated prediction of RNA 3D structures**, particularly for large RNA molecules.  
The method is inspired by **machine translation**, where RNA secondary structure elements are translated into tertiary structure fragments using the RNA FRABASE database.

This fragment-based strategy enables efficient and scalable RNA 3D structure modeling while maintaining biologically realistic geometries.

---

## Operating Modes

RNAComposer operates in two distinct modes:

### Interactive Mode

- Designed for modeling **one RNA molecule at a time**
- Supports RNA sequences up to **500 nucleotides**
- Produces **a single 3D RNA structure model**
- Accepts the following inputs:
  - RNA sequence **and** secondary structure (dot-bracket notation)
  - RNA sequence only (introductory example)

This mode is suitable for individual RNA structure prediction and exploratory use.

---

### Batch Mode

- Designed for **large-scale automated RNA structure modeling**
- Supports RNA sequences up to **500 nucleotides**
- Allows submission of **up to 10 RNA sequences per job**
- Requires **user-defined RNA secondary structures**
- Available **only for registered users**

Batch mode is intended for high-throughput modeling applications.

---

## Usage Notes

- RNAComposer relies on **RNA secondary structure information** for optimal performance.
- Prediction accuracy depends on the correctness of the provided secondary structure and the availability of structural motifs in the FRABASE database.
- Output structures are typically provided in **PDB format**.

---

## Citation

If you use RNAComposer in your research, **please cite the following publications**:

```bibtex
@article{sarzynska2023rnacomposer,
  title={RNA tertiary structure prediction using RNAComposer in CASP15},
  author={Sarzynska, Justyna and Popenda, Michal and Antczak, Maciej and Szachniuk, Marta},
  journal={PROTEINS: Structure, Function, and Bioinformatics},
  volume={91},
  number={12},
  pages={1790--1799},
  year={2023},
  doi={10.1002/prot.26578}
}

@article{popenda2012automated,
  title={Automated 3D structure composition for large RNAs},
  author={Popenda, Michal and Szachniuk, Marta and Antczak, Maciej and Purzycka, Katarzyna J. and Lukasiak, Piotr and Bartol, Natalia and Blazewicz, Jacek and Adamiak, Ryszard W.},
  journal={Nucleic Acids Research},
  volume={40},
  number={14},
  pages={e112},
  year={2012},
  doi={10.1093/nar/gks339}
}
