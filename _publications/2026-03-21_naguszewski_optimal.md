---
list_title: "[15] Optimal parallelisation strategies for flat histogram Monte Carlo sampling"
title: "Optimal parallelisation strategies for flat histogram Monte Carlo sampling"
published: journal
authors: 'H. J. Naguszewski, <u>C. D. Woodgate</u>, D. Quigley'
date: 2026-03-21
collection: publications
venue: "Computer Physics Communications <b>324</b>, 110125"
paperurl: "https://doi.org/10.1016/j.cpc.2026.110125"
arXiv: "arXiv:2510.11562"
arXivurl: "https://arxiv.org/abs/2510.11562"
---

<h3>Abstract</h3>
Flat histogram methods, such as Wang–Landau sampling, provide a means for high-throughput calculation of phase diagrams of atomistic/lattice model systems. Many parallelisation schemes with varying degrees of complexity have been proposed to accelerate such sampling simulations. In this study, several widely used schemes are benchmarked - both in isolation and in combination - to establish best practice. The schemes studied include energy domain decomposition with both static sizing of energy sub-domains, as well as a dynamic sub-domain sizing scheme which we propose. We also assess the benefits both of replica exchange and of including multiple random walkers per sub-domain, to determine which factors have the largest impact on parallel efficiency. Additionally, the influence of energy sub-domain overlap regions is discussed. As illustrative test cases, we implement and apply the aforementioned strategies to a lattice-based model describing the internal energy of a substitutional alloy, studying the AlTiCrMo refractory high-entropy superalloy as well as the binary CuZn system, both of which crystallographically order into a B2 (CsCl) structure with decreasing temperature. We find that - while all of the proposed strategies confer a non-negligible speedup - parallelisation across energy domains which are non-uniform in size offers the most appreciable performance improvements. This work offers concrete recommendations for which parallelisation strategies should be prioritised to optimally accelerate flat-histogram Monte Carlo simulations.
