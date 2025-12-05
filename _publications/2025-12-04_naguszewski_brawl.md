---
list_title: "[12] BraWl: Simulating the thermodynamics and phase stability of multicomponent alloys using conventional and enhanced sampling techniques"
title: "BraWl: Simulating the thermodynamics and phase stability of multicomponent alloys using conventional and enhanced sampling techniques"
published: journal
authors: 'H. J. Naguszewski, L. B. Partay, D. Quigley, <u>C. D. Woodgate</u>'
date: 2025-12-04
collection: publications
arXiv: "arXiv:2505.05393"
arXivurl: "https://doi.org/10.48550/arXiv.2505.05393"
venue: "Journal of Open Source Software <b>10</b>, 8346"
paperurl: "https://doi.org/10.21105/joss.08346"
---

<h3>Abstract</h3>
Many technologically relevant materials, both structural and functional, are ‘alloys’ - systems in which two or more (typically) metallic elements are combined to produce a new material with desirable physical properties. In a substitutional alloy, there is a fixed underlying crystal lattice, while the probability of a given constituent element of the alloy occupying a particular lattice site is determined by thermodynamic considerations. In accordance with these considerations, atoms in an alloy can arrange themselves differently depending on the precise chemical composition and processing conditions. Frequently, a mixture of elements will form a regular crystalline lattice with substitutional disorder (a ‘solid solution’) at high temperature, before atomic short- and long-range order emerges as the material is cooled. The nature of atomic arrangements in a material determines many important physical properties. For a given combination of elements, it is therefore crucial to understand the nature of atomic ordering in a material, as well as the temperature at which it emerges upon cooling, to guide materials processing strategies. One physically intuitive model for the internal energy of an alloy is the Bragg-Williams model, which assumes that atoms in the alloy interact in a pairwise manner.  Crucially, the atom-atom effective pair interactions (EPIs) which appear in the Bragg-Williams Hamiltonian can be obtained <i>ab initio</i> using density functional theory (DFT) calculations.  When appropriate sampling techniques are applied to the Bragg-Williams model, it is possible to explore the configuration space of a given alloy in detail and determine equilibrium phases as a function of temperature, leading to construction of phase diagrams. Here, we present BraWl, a Fortran package implementing a range of conventional and enhanced sampling algorithms for exploration of the phase space of the Bragg-Williams model, facilitating study of diffusional solid-solid transformations in binary and multicomponent alloys. These sampling algorithms include Metropolis-Hastings Monte Carlo, Wang-Landau sampling, and Nested Sampling. We demonstrate the capabilities of the package by applying it to some prototypical binary and multicomponent alloys, including high-entropy alloys.
