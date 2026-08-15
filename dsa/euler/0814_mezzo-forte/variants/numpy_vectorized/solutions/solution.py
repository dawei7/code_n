"""Project Euler Problem 814: Mezzo-Forte (NumPy Transfer Matrix Variant).

Mathematical Formulation:
4n choir member mutual visibility arrangements evaluated via transfer matrix exponentiation.
"""

from __future__ import annotations

import numpy as np


def solve(n: int = 1000, mod: int = 1000000007) -> str:
    """Compute arrangement count mod (10^9+7) using NumPy matrix exponentiation."""
    # 4x4 state transition transfer matrix
    T = np.array([
        [1, 1, 0, 1],
        [1, 2, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 2]
    ], dtype=object)

    # Matrix power modulo mod
    res = np.eye(4, dtype=object)
    base = T
    p = 4 * n
    while p > 0:
        if p & 1:
            res = (res @ base) % mod
        base = (base @ base) % mod
        p >>= 1

    total_trace = int(np.trace(res) % mod)
    return str(total_trace)


if __name__ == "__main__":
    print(solve())
