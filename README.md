# My Project

Works done as part of the VERITAS collaboration in the Summer of 2021 (McGill University).

Goal of the project is to use the python-based Gammapy package to validate the analysis of the properties of various astorphysical sources studied under the VERITAS Collaboration (https://veritas.sao.arizona.edu).

Analysis of the sources:
- Crab (Nebula)
- 1ES 1959+650 (HBL: Blazars)
- LS5039 / HESS J1826-148 (LBL: Binary system)
- MRK501 (HBL: Blazars)
- RGBJ0710+591 (HBL: Blazars)
- Boomerang (Nebula)

The Crab Nebula is the most important source for validation, as it represents the most luminous and studied source of the VERITAS database. It was also the only source at the time with coast-to-coast runlist. 

Other sources like the BL Lac (HBL) are also very luminous making them ideal for validation. 

The LS5039 / HESS J1826-148 is the analysis of a binary system

Boomerang at the time was a recent source found and did not have many runlist. It provides the opportunity to study newer sources with Gammapy.



### FOR NON-VERITAS MEMBERS
I cannot provide the runlist data for any of these sources, thus the code cannot be run. 

### FOR VERITAS MEMBERS
 `runlist_investigated.csv` contains all the runlist data investigated for the different sources. Typically, I pick the most luminous runlist for each of the sources. Also, I produced a code to generate the background fit files; it is available on the VERITAS wiki.



## Installation

To install the project, you can use the following command:



pip install gammapy==0.18.2

pip install astropy==4.2.1

pip install matplotlib pandas numpy astropy scipy

(VERSION VALID IN MAY 2021, NEWER VERSION MIGHT CAUSE ISSUES)

## Usage





