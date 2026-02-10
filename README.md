# A computationally efficient physics-informed DMD-based acceleration method for Monte Carlo neutronics and thermal-hydraulics coupling simulations

This repository contains the source code and the executable program for the paper.

## 1. Source Code Description
Due to confidentiality requirements, the **High-Fidelity Module** cannot be disclosed. Additionally, the **Pc-DMD Module** is not detailed here as it has been verified in previous literature.

Therefore, the provided source code primarily focuses on the implementation of the proposed coupling algorithm and the adaptive strategies. The key files are described as follows:

* **`pyDMD.py`**
    The DMD algorithm for predicting power field.

* **`automatic_core.py`**
    The Monte Carlo neutronics and thermal-hydraulics coupling system for the core model.

* **`automatic_assembly.py`**
    The Monte Carlo neutronics and thermal-hydraulics coupling system for the assembly model.


## 2. Executable Program
**`COBRA.exe`** is a proprietary program developed by our team, which integrates the algorithm proposed in the paper.

To reproduce the calculation results presented in the paper:
1. Download the executable directly from the [**Releases**](../../releases) page.
2. Run the program.
3. When prompted, input **`mox`** or **`uo2`**.

---
**Affiliation:** China Three Gorges University
