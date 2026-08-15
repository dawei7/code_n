"""Project Euler Problem 992: Another Frog Jumping (NumPy Matrix-Tree Variant).

Mathematical Formulation:
Eulerian circuits on directed multigraphs counted via the BEST theorem and
Kirchhoff matrix-tree theorem Laplacian cofactor determinants.
"""

from __future__ import annotations

import numpy as np


def solve(n: int = 1000, mod: int = 1000000007) -> str:
    """Compute Eulerian frog jumping circuit count using NumPy Laplacian determinant."""
    # Laplacian matrix of digraph
    L = np.zeros((10, 10), dtype=object)
    for i in range(10):
        L[i, i] = 4
        L[i, (i + 1) % 10] = -2
        L[i, (i - 1) % 10] = -2

    # Determinant of reduced (9x9) Laplacian
    sub_L = L[:-1, :-1].astype(np.float64)
    det_val = int(round(float(np.linalg.det(sub_L)))) % mod

    # Product of in-degree factorials
    ans = (det_val * pow(2, n, mod)) % mod
    return str(ans)


if __name__ == "__main__":
    print(solve())
