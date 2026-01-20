# 3dRNA v2.0 (3dRNA_DNA)

## Overview

**3dRNA v2.0 (3dRNA_DNA)** is an automatic, fast, and high-accuracy method for **RNA and DNA tertiary structure prediction**.  
The method constructs three-dimensional structures using **sequence and secondary structure information**, assembling structures from **template segments** derived from experimentally determined RNA and DNA structures.

3dRNA_DNA supports both **de novo segment construction** and **template-based modeling**, enabling efficient prediction and refinement of nucleic acid 3D structures.

---

## Web Server

- **3dRNA v2.0 Web Server**  
  [http://biophy.hust.edu.cn/new/3dRNA](http://biophy.hust.edu.cn/new/3dRNA)

---

## Method Description

The 3dRNA_DNA framework builds RNA and DNA tertiary structures through a **segment-based assembly strategy**.  
The core idea is to decompose the target secondary structure into structural segments, retrieve suitable templates from a curated structural library, and assemble them into a complete 3D model.

The template library is constructed from **high-resolution crystal and NMR structures**, ensuring physically realistic geometries.

---

## Main Modeling Pipeline

The main routines of **3dRNA_DNA** include:

1. **Secondary Structure Decomposition**  
   The input RNA or DNA secondary structure is decomposed into individual structural segments.

2. **Template Searching**  
   For each segment, a corresponding template is retrieved from the template library derived from crystal and NMR structures.

3. **Ab Initio Segment Construction**  
   If no suitable template is available, a **distance-geometry-based loop building method** is applied to construct the segment *ab initio*.

4. **Structure Assembly**  
   A random template is selected for each segment, and all segments are assembled to generate the final RNA or DNA 3D structure.

---

## Structure Optimization

In addition to structure assembly, **3dRNA_DNA** provides a refinement procedure:

- **Simulated Annealing Monte Carlo (SAMC)** optimization  
- Further improves structural geometry and global topology  
- Can be applied to both predicted and user-provided structures

This optimization step enhances the accuracy and physical realism of the predicted models.

---

## Key Features

- Automated RNA and DNA 3D structure prediction
- Template-based and *ab initio* hybrid modeling
- Supports secondary-structure-guided modeling
- Simulated annealing–based structure refinement
- Fast and suitable for large-scale modeling

---

## Usage Notes

- Accurate **secondary structure input** significantly improves prediction quality.
- Output structures are typically provided in **PDB format**.
- Refinement using simulated annealing is recommended for high-accuracy applications.

---

## Reference

If you use **3dRNA v2.0 (3dRNA_DNA)** in your research, please cite the original publication describing the method.

(Reference information can be added here if required.)
