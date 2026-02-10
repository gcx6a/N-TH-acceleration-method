# An Online Adaptive Pc-DMD Algorithm with Grassmann Manifold Spatial Mapping

This repository contains the source code and the executable program for the paper.

## 1. Executable Program (AMAC.exe)
**`AMAC.exe`** is a proprietary program developed by our team, which integrates the algorithm proposed in the paper.

To reproduce the calculation results presented in the paper:
1. Download the executable directly from the [**Releases**](../../releases) page.
2. Run the program.
3. When prompted, input **`mox`** or **`uo2`**.

## 2. Source Code Description
Due to confidentiality requirements, the **High-Fidelity Module** cannot be disclosed. Additionally, the **Pc-DMD Module** is not detailed here as it has been verified in previous literature.

Therefore, the provided source code primarily focuses on the implementation of the proposed coupling algorithm and the adaptive strategies. The key files are described as follows:

* **`CouplingStrategyDMD.cpp`**
    The main workflow of the entire algorithm, handling the coupling logic.

* **`ProcessDataWithPCA.cpp`**
    Performs Principal Component Analysis (PCA) on the simulation data.

* **`AdaptiveCluster.cpp`**
    Implements the adaptive clustering algorithm.

* **`FindInterpolationData.cpp`**
    Identifies the specific regions that require reconstruction.

* **`GrassmannDistance.cpp`**
    Calculates the coefficients for reconstruction based on the distance between two points on the Grassmann manifold.

---
**Affiliation:** China Three Gorges University
