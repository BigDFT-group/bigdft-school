# BigDFT School project.

This project contans the material for training about BigDFT code which could be execute via Google colab.
There are multiple ways to run these notebooks. You have to open a google colab session and Start by the Installation tutorial.

To do that:

 1. Go here with your google account: https://colab.research.google.com/
 2. File-> Open Notebook - > GitHub
 3. `BigDFT-group/bigdft-school`
 4. Start from the first Notebook of the chosen directory.

**Alternative method (for colab experts):** It is also possible to open this project from a GitHub fork. To do this it would be enough to open one of the notebooks in the github page of 
your fork and replace `github.com` with `githubtocolab.com` in the url page. With this technique it would be possible to push your notebooks into a suitable branch of the github fork.

Such notebooks can also be executed on a local workstation with the bigdft-client installed.
The installation can be performed by running the command

``
pip install pybigdft pyfutile py3dmol remotemanager
``

In case you do not have a jupyter notebook environment installed on your workstation, you can issue the command:

``
pip install jupyterlab py3dmol seaborn
``

The notebook can also run on a colab session, with the run data imported.

Here follow the programs of the Schools that can have been done with this material

# Program of BigDFT training of Winter School in Computational Chemistry (2024)

45 Min: Introduction and presentation of BigDFT formalism

15 Min: Presentation of Coogle Colab and dry-run approach Quick Start - Initial Walkthrough

45 Min ("Slow-Motion" walkthrough) Basic Tutorials - 1.A.B.C.G.H.(J) 
(https://github.com/BigDFT-group/bigdft-school/tree/main/CCP_tutorials) - Ex. Replacement of 1.B with the anthracene dimer
Sam

30 Min Towards Large Scale calculations - Linear Scaling algorthm - Complexity Reduction - Fragments  -  Application WD

30 Min 2.A.B.C WD 4A - LG 

15 min Closing Remarks (Features + tutorials)  (remotemanager - Implicit Solvents - TCDFT)  - LG


# Program of ENCCS Training half-day on BigDFT in HPC (directory Enccs_tutorials)

|  Time       | Section | 
| ---- | ----- | 
|09:00-09:30 | Introduction to BigDFT (Presentation - Luigi Genovese & Laura Ratcliff)|
|09:30-10:00 | Introduction to PyBigDFT: Notebook 1. System Manipulation (Walkthrough - Martina Stella)|
|10:00-10:30 | Remote Runner (Presentation & Walkthrough/Hands On - NB 2. - Louis Beal)|
|10:30 - 11:00 | Coffee break|
|11:00 - 12:00 | Cubic Scaling BigDFT (Hands On (NB 3.) - Luigi Genovese)|
|12:00 - 13:00 | Linear Scaling BigDFT (Hands On (NB 4.) - Laura Ratcliff)|



# Program of CCP-BioSim Training Day on BigDFT code (directory CCP_tutorials)

Morning session: 9h

9h-9:30h introduction (wavelets, DFT, what you can do with BigDFT) Talk 

9h30-11h Set up of the training
* 0.Installation 
* 1.A.Systems
* 1.B.Calculations
* 1.C.Logfiles
* Other exercises (if time allows)

11h-11h30
Linear Scaling and Complexity Reduction Talks

11h30-12h30
* 2.A.InitialRunsLinear
* 2.B.LinearScaling

Lunch: 12h30 - 13h30

13h30-14h00
* 2.C.ComplexityReduction 

14h – 14h20
Implicit Solvent (Poisson Solver) talk

14h20-14h55
* 3.A.ImplicitSolvent

14h55-15h25 
Extensions to LS : Fragments and T-CDFT

15h25-16h15
* 4.A.MolecularFragments
* 4.B.EmbeddedFragments
* 4.C.TCDFTNaphthalene

16h15-16h30
Concluding remarks 

