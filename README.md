# A computationally efficient physics-informed DMD-based acceleration method for Monte Carlo neutronics and thermal-hydraulics coupling simulations

This repository contains the source code and the executable program for the paper.

## 1. Source Code Description
The main files are described as follows:

* **`pyDMD.py`**
    The DMD algorithm for predicting power field.

* **`automatic_core.py`**
    The Monte Carlo neutronics and thermal-hydraulics coupling system for the core model.

* **`automatic_assembly.py`**
    The Monte Carlo neutronics and thermal-hydraulics coupling system for the assembly model.

## 2. Executable Program
The Monte Carlo reactor code OpenMC is available at the following GitHub repository: https://github.com/openmc-dev/openmc.git.

The program file is described as follows:

**`COBRA.exe`** is an executable file for a thermal-hydraulics program.

To reproduce the calculation results presented in the paper:
1. Ensure computing equipment has the neutronics program OpenMC and the thermal-hydraulics program COBRA available.
2. Build neutronics Model and thermal-hydraulics Model.
3. Select the corresponding coupling system model and fill in the input files within it.
4. Perform neutronics and thermal-hydraulics coupling calculation using the DMD algorithm under physical constraints.

---
**Affiliation:** China Three Gorges University
