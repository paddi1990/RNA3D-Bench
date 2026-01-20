# SimRNA

## Overview

**SimRNA** is a computational method for **RNA three-dimensional (3D) structure modeling** with **optional restraints**.  
It is designed to efficiently explore RNA conformational space and identify biologically relevant structures through **coarse-grained modeling and stochastic sampling**.

SimRNA combines:
1. A **coarse-grained representation** of RNA,
2. **Monte Carlo–based sampling** of conformational space,
3. A **statistical potential** to approximate RNA folding energy and guide structure selection.

This framework enables large-scale RNA folding simulations, structure prediction, and analysis of RNA folding landscapes.

---

## Web Server and Software

- **SimRNAweb**  
  Web server for RNA folding simulations and 3D structure modeling with optional restraints.  
  [https://genesilico.pl/SimRNAweb/](https://genesilico.pl/SimRNAweb/)

- **Standalone SimRNA**  
  To download the standalone version of SimRNA, visit:  
  [https://genesilico.pl/software/stand-alone/simrna/](https://genesilico.pl/software/stand-alone/simrna/)

---

## Method Description

SimRNA represents RNA molecules using a **reduced, coarse-grained model**, significantly lowering computational cost while retaining key structural features.  
Conformational sampling is performed using the **Monte Carlo method**, and candidate structures are evaluated with a **knowledge-based statistical potential** derived from experimentally determined RNA structures.

This approach allows SimRNA to efficiently sample folded, partially folded, and unfolded RNA conformations.

---

## Restraints and New Features (December 2023)

Recent updates have substantially extended the functionality of SimRNA by introducing **diverse and flexible restraints** and enhanced analysis capabilities.

### Incorporation of Diverse Restraints

SimRNA now supports a broad range of restraints, including:

- **Soft restraints on secondary structure** (Dec. 2023)
- **Hard restraints on base pairs** (Dec. 2023)
- **Soft restraints on base pairs** (Dec. 2023)
- **Restraints on unpaired residues**
- **Restraints derived from chemical probing data** (Dec. 2023)
- **Exclusion of Watson–Crick edges for base pairing** (Dec. 2023)
- Support for both **canonical and non-canonical base pairs**

These restraints enable more accurate modeling and integration of experimental data.

---

### Advanced Control over Simulation Parameters

- A new restraint definition framework allows modeling of **alternative RNA conformations**
- Increased control over simulation parameters enables:
  - Conformational space searching
  - RNA folding simulations
  - RNA unfolding simulations

(Released Dec. 2023)

---

### Enhanced Data Processing and Analysis

- Expanded options for **clustering folding trajectories**
- Generation of **representative models** from simulation ensembles
- Ability to **reanalyze the same simulation multiple times** using different parameters
- Facilitates deeper exploration of RNA folding landscapes

(Released Dec. 2023)

---

## Key Features

- RNA 3D structure prediction using coarse-grained modeling
- Monte Carlo–based conformational sampling
- Statistical potential–based energy evaluation
- Extensive support for experimental and theoretical restraints
- Folding trajectory analysis and clustering
- Suitable for both prediction and folding landscape exploration

---

## Usage Notes

- Restraints significantly improve prediction accuracy when reliable experimental or secondary structure data are available.
- SimRNA can be used for **de novo structure prediction**, **structure refinement**, and **folding pathway analysis**.
- Output models are typically provided in **PDB format** after reconstruction from coarse-grained representations.

---

## Citation

If you use **SimRNA** or **SimRNAweb** in your research, please cite the appropriate publications:

```bibtex
@article{moafinejad2024simrnaweb,
  title={SimRNAweb v2.0: A web server for RNA folding simulations and 3D structure modeling, with optional restraints and enhanced analysis of folding trajectories},
  author={Moafinejad, S. Naeim and de Aquino, Belisa R. H. and Boniecki, Micha{\l} J. and Pandaranadar Jeyeram, Iswarya P. N. and Nikolaev, Grigory and Magnus, Marcin and Amiri Farsani, Masoud and Badepally, Nagendar Goud and Wirecki, Tomasz K. and Stefaniak, Filip and Bujnicki, Janusz M.},
  journal={Nucleic Acids Research},
  year={2024},
  doi={10.1093/nar/gkw279}
}

@article{magnus2016simrnaweb,
  title={SimRNAweb: a web server for RNA 3D structure modeling with optional restraints},
  author={Magnus, Marcin and Boniecki, Micha{\l} J. and Dawson, William and Bujnicki, Janusz M.},
  journal={Nucleic Acids Research},
  year={2016},
  doi={10.1093/nar/gkae356}
}

@article{boniecki2015simrna,
  title={SimRNA: a coarse-grained method for RNA folding simulations and 3D structure prediction},
  author={Boniecki, Micha{\l} J. and Lach, Grzegorz and Dawson, William K. and Tomala, Karol and Lukasz, P. and Soltysinski, Tomasz and Rother, Krzysztof M. and Bujnicki, Janusz M.},
  journal={Nucleic Acids Research},
  year={2015},
  doi={10.1093/nar/gkv1479}
}
