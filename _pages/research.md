---
permalink: /research/
title: "Research"
excerpt: "Research"
author_profile: true
redirect_from: 
  - /research_interests/
  - /research_interests
---

My research sits at the intersection of [electronic structure theory](https://en.wikipedia.org/wiki/Electronic_band_structure), [atomistic materials simulation](https://en.wikipedia.org/wiki/Molecular_modelling), and [statistical physics](https://en.wikipedia.org/wiki/Statistical_mechanics). I develop and apply modelling approaches for studying a range of alloys and magnetic materials, with a particular focus on appropriate treatment of disorder and finite-temperature effects. Classes of physical system on which I have previously worked include [high-entropy alloys](https://en.wikipedia.org/wiki/High-entropy_alloy) and rare-earth-free [permanent magnets](https://en.wikipedia.org/wiki/Magnet). I am also particularly interested in the development of new methods for materials simulation, and in writing software implementing those methods. Below I outline, in detail, four connected strands of my research, along with some selected publications.

## Alloys

A significant portion of my work focuses on understanding how alloys (particularly multicomponent and 'high-entropy' alloys) choose to order, segregate, or remain disordered depending on their composition and processing temperature. I approach this primarily from the perspective of first-principles electronic structure calculations, where I use [density functional theory (DFT)](https://en.wikipedia.org/wiki/Density_functional_theory) calculations combining the all-electron Korringa-Kohn-Rostoker (KKR) method, the coherent potential approximation (CPA), and a perturbative concentration wave analysis. (Though I also use a range of atomistic models and simulation methods, too!) This unusual combination of tools allows me to quantify both atomic short-range order in solid solutions as well as to predict chemical disorder-order transitions in a way that gives insight into the underlying physics. In particular, I aim to connect atomic ordering tendencies to mechanistic drivers in an alloy's electronic structure, such as features in the density of states around the Fermi level and element-specific bonding preferences, with the aim of giving qualitative insights that are transferable across across the space of possible alloy compositions.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/alloy_intermetallic_segregation.jpg" alt="Illustration of possible atomic configurations for a two-dimensional 'alloy'.">
  <figcaption>Illustration of possible atomic configurations for a two-dimensional 'alloy'. Much of my research on alloys focusses on studying diffusional, solid-solid phase transformations which can occur as a material is cooled from high temperatures.</figcaption>
</figure> 

### Selected publications
* <b>C. D. Woodgate</b>, D. Hedlund, L. H. Lewis, J. B. Staunton, <i>"Interplay between magnetism and short-range order in medium- and high-entropy alloys: CrCoNi, CrFeCoNi, and CrMnFeCoNi,"</i> [Physical Review Materials <b>7</b>, 053801 (2023)](https://doi.org/10.1103/PhysRevMaterials.7.053801).
* <b>C. D. Woodgate</b>, G. A. Marchant, L. B. Partay, J. B. Staunton, <i>"Structure, short-range order, and phase stability of the AlxCrFeCoNi high-entropy alloy: Insights from a perturbative, DFT-based analysis",</i> [npj Computational Materials <b>10</b>, 271 (2024)](https://doi.org/10.1038/s41524-024-01445-w).
* X. Zhang, <b>C. D. Woodgate</b>, G. Hadjipanayis, J. B. Staunton, L. H. Lewis, <i>"Tailoring microstructures with mild magnetic-field processing: A case study of CuNiFe alloys",</i> [Acta Materialia <b>307</b>, 121965 (2026)](https://doi.org/10.1016/j.actamat.2026.121965).

## Magnetic materials
In magnetism, I am particularly interested in simulating how thermally-induced spin fluctuations can modify the electronic structure and physical properties of materials. Much of my previous work has focussed on on hard magnetic materials, _i.e._ permanent magnets, where I have worked extensively on modelling of the atomically ordered L1<sub>0</sub> phase of FeNi, also known as the meteoritic mineral [tetrataenite](https://en.wikipedia.org/wiki/Tetrataenite). In this system, using fully relativistic DFT and appropriate techniques for averaging over compositional and magnetic disorder, I’ve looked in detail at how the material's magnetocrystalline anisotropy energy (determining how strong a magnet is) depends on composition, chemical order, and temperature. I am fortunate to enjoy a close collaboration with the experimental group of [Prof. Laura H. Lewis](https://coe.northeastern.edu/people/lewis-laura/) at Northeastern University (Boston, USA), with whom I work on FeNi and other technologically relevant magnetic materials. More recently, I have also engaged with the experimental group of [Dr. Alannah M. Hallas](https://qmi.ubc.ca/team-member/alannah-hallas/) at the University of British Columbia (Vancouver, Canada), whose group works extensively on magnetic materials with strong correlations and complex physics, such as high-entropy oxides and altermagnets. For me, engaging with experimental groups is the key to delivering impactful research; the point is to go beyond isolated _computation_ of magnetic properties and instead to give insight into what controls them and, therefore, which experimental levers can be pulled to engineer new materials with potentially desirable properties.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/magnetic_disorder.jpg" alt="Illustration of atomically localised magnetic moments disordering with increasing temperature.">
  <figcaption>Illustration how atomically localised magnetic moments in a ferromagnet can disorder with increasing temperature, <i>T</i>, and corresponding evolution of some magnetic order parameter, <i>m</i>. Zero temperature corresponds to pristine order, while above the Curie temperature, <i>T</i><sub>C</sub>, magnetic moments are disordered.</figcaption>
</figure> 

### Selected publications
* <b>C. D. Woodgate</b>, C. E. Patrick, L. H. Lewis, J. B. Staunton, <i>"Revisiting Néel 60 years on: the magnetic anisotropy of L1<sub>0</sub> FeNi (tetrataenite)",</i> [Journal of Applied Physics <b>134</b>, 163905 (2023)](https://doi.org/10.1063/5.0169752).
* <b>C. D. Woodgate</b>, L. H. Lewis, J. B. Staunton, <i>"Integrated ab initio modelling of atomic ordering and magnetic anisotropy for design of FeNi-based magnets,"</i> [npj Computational Materials <b>10</b>, 272 (2024)](https://doi.org/10.1038/s41524-024-01435-y).

## Interface of electronic structure calculations with atomistic models and machine-learning techniques
A recurring goal in my research is to interface high-fidelity (but often computationally demanding) electronic structure calculations with atomistic and/or surrogate models capable of simulation of phenomena at larger length and/or timescales than would usually be accessible to electronic structure theorists. For example, the concentration-wave formalism I use to study alloy thermodynamics produces atom-atom effective pair interactions directly from KKR-CPA, and I then pass those into lattice-based Hamiltonians that can be sampled to study phase transitions and phase equilibria in fine detail. Additionally, I’m also increasingly interested in machine-learning approaches based on electronic structure data. For example, in recent collaborative work, I’ve helped to develop [machine-learned interatomic potentials (MLIPs)](https://en.wikipedia.org/wiki/Machine-learned_interatomic_potential) for chemically disordered alloys, facilitating simulation of a variety of phenomena which would be computationally demanding to study directly using DFT. The motivation here is to be able to perform simulations whose accuracy approaches that of DFT for significantly reduced computational cost, especially in systems where both chemical disorder and magnetism matter.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/em_protocol.png" alt="Illustration of the workflow we used when developing a machine-learned interatomic potential for Fe-Cr-Ni alloy.">
  <figcaption>Illustration of the workflow we used when developing a machine-learned interatomic potential for Fe<sub>7</sub>Cr<sub>2</sub>Ni alloy - a prototypical composition for austenitic stainless steel. Reproduced from Phys. Rev. Mater. <b>8</b>, 033804 (2024).</figcaption>
</figure> 

### Selected publication
* L. Shenoy, <b>C. D. Woodgate</b>, J. B. Staunton, <i>et al.</i>, <i>"A collinear-spin machine-learned interatomic potential for Fe<sub>7</sub>Cr<sub>2</sub>Ni alloy,"</i> [Physical Review Materials <b>8</b> 033804 (2024)](https://doi.org/10.1103/PhysRevMaterials.8.033804).

## Method development and best practices in materials simulation
Method development is an area which is particularly important to me, because I think chemical disorder, magnetic disorder, and finite temperature effects are still poorly-served by many standard materials simulation and electronic structure workflows. In addition to my work on the application of concentration waves to the study of the phase stability of high-entropy alloys, I've also worked on the development of software tools which facilitate the application of various conventional and enhanced sampling techniques to study chemical disorder-order transitions in alloys when their internal energy is described using some atomistic model or 'pair potential'. Finally, I remain interested in establishing best practice in materials simulation, to ensure that computing resources are being utilised as efficiently as possible. A recent highlight in this area is work benchmarking various proposed parallelisation schemes for the widely-utilised Wang-Landau Monte Carlo sampling algorithm.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/wl_parallelisation.jpg" alt="Some parallelisation schemes for the Wang-Landau sampling algorithm.">
  <figcaption>Sketch of some of the parallelisation strategies for the Wang-Landau sampling algorithm which we benchmarked in recent work. Reproduced from arXiv:2510.11562.</figcaption>
</figure> 

### Selected publications
* H. J. Naguszewski, L. B. Partay, D. Quigley, <b>C. D. Woodgate</b>, <i>"BraWl: Simulating the thermodynamics and phase stability of multicomponent alloys using conventional and enhanced sampling techniques,"</i> [Journal of Open Source Software <b>8</b>, 8346 (2025)](https://doi.org/10.21105/joss.08346).
* H. J. Naguszewski, <b>C. D. Woodgate</b>, D. Quigley, <i>"Optimal parallelisation strategies for flat histogram Monte Carlo sampling,"</i> [arXiv:2510.11562](https://doi.org/10.48550/arXiv.2510.11562).
