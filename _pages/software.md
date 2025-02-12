---
permalink: /software/
title: "Software"
excerpt: "Software"
author_profile: true
redirect_from: 
  - /codes/
---

I have experience of developing scientific software in Python, C, C++, and Fortran. Often these are small codes performing analysis of simulation outputs and/or toy calculations, but I also develop and release my own packages on [GitHub](https://github.com/chriswoodgate). I have experience of developing codes suitable for deployment on high-performance computing facilities, including use of both shared memory (OpenMP) and distributed memory (MPI) parallelism. I also have some experience in the use of Nvidia's CUDA platform for GPU acceleration. If you are interested in working with me on a software project, please [email me](mailto:christopher.woodgate@physics.org)!

Codes Developed
-----
* [BraWl](https://github.com/ChrisWoodgate/BraWl).
  * A code for performing fast, lattice-based Monte Carlo simulations to study atomic arrangements in multicomponent alloys, with an internal energy given by a Bragg-Williams Hamiltonian.
  * The code primarily uses the Metropolis algorithm with Kawasaki dynamics. It can be used for simulated annealing (to search for and study predicted phase transitions) but also to draw decorrelated atomic configurations for use in subsequent studies, *e.g.* in training datasets for machine-learned interatomic potentials.
  * Recently, working with [Dr Livia Bartók-Pártay](https://warwick.ac.uk/fac/sci/chemistry/staff/liviabartokpartay/) (Department of Chemistry, University of Warwick), we implemented the [nested sampling algorithm](https://en.wikipedia.org/wiki/Nested_sampling_algorithm), which facilitates a complete, unbiased exploration of arbitrary potential energy surfaces.
  * As of 2025, the code also features a parallelised implementation of Wang–Landau sampling following work conducted with [Hubert Naguszewski](https://warwick.ac.uk/fac/sci/hetsys/people/studentscohort4/naguszewski/) and [Prof. David Quigley](https://warwick.ac.uk/fac/sci/physics/staff/research/dquigley/) (Department of Physics, University of Warwick).

Codes Used
-----
I am familiar a number of community-developed density functional theory (DFT) codes, including [CASTEP](http://www.castep.org), [JuKKR](https://jukkr.fz-juelich.de), [SPR-KKR](https://www.ebert.cup.uni-muenchen.de/old/), [Hutsepot](https://hutsepot.jku.at), and [MARMOT](https://warwick.ac.uk/marmotcode). I also have experience of using the [Atomic Simulation Environment (ASE)](https://wiki.fysik.dtu.dk/ase/) to build workflows and `drive' codes in a more automated manner.
