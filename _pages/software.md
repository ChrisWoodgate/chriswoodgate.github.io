---
permalink: /software/
title: "Software"
excerpt: "Software"
author_profile: true
redirect_from: 
  - /codes/
---

I have experience of developing scientific software in Python, C, C++, and Fortran. Quite frequently I write small codes for performing analysis of simulation outputs and/or running toy calculations, but I also develop and release my own (more fully-featured) packages on [GitHub](https://github.com/chriswoodgate). Additionally, you will occasionally find me making contributions to other people's codebases - usually implementing features I would like to use myself!

I have experience of developing codes suitable for deployment on high-performance computing facilities, including use of both shared memory (OpenMP) and distributed memory (MPI) parallelism. I also have some experience in the use of Nvidia's CUDA platform for GPU acceleration. If you are interested in working with me on a software project, please [email me](mailto:christopher.woodgate@physics.org)!

Codes Developed
-----
* [BraWl](https://github.com/ChrisWoodgate/BraWl), released open-source under the GNU Lesser General Public License (LGPL).
  * A package for performing lattice-based atomistic simulations of alloys with an internal energy given by a Bragg-Williams Hamiltonian. The package implements a range of conventional and enhanced sampling techniques, including:
    * The [Metropolis-Hastings](https://en.wikipedia.org/wiki/Metropolis–Hastings_algorithm) Monte Carlo algorithm.
    * The [Nested Sampling](https://en.wikipedia.org/wiki/Nested_sampling_algorithm) algorithm, implemented in collaboration with the group of [Dr Livia Bartók-Pártay](https://warwick.ac.uk/fac/sci/chemistry/staff/liviabartokpartay/) (Department of Chemistry, University of Warwick).
    * [Wang-Landau sampling](https://en.wikipedia.org/wiki/Wang_and_Landau_algorithm), a parallel implementation of which is available following work conducted with [Hubert Naguszewski](https://warwick.ac.uk/fac/sci/hetsys/people/studentscohort4/naguszewski/) and [Prof. David Quigley](https://warwick.ac.uk/fac/sci/physics/staff/research/dquigley/) (Department of Physics, University of Warwick).

Codes Used
-----
I am familiar with several community-developed density functional theory (DFT) codes, including [CASTEP](http://www.castep.org), [JuKKR](https://jukkr.fz-juelich.de), [SPR-KKR](https://www.ebert.cup.uni-muenchen.de/old/), [Hutsepot](https://hutsepot.jku.at), and [MARMOT](https://warwick.ac.uk/marmotcode). I also have experience of using the [Atomic Simulation Environment (ASE)](https://wiki.fysik.dtu.dk/ase/) to build workflows and `drive' codes in a more automated manner.
