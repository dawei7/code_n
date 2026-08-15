"""Project Euler Problem 1000: Meta-Problem 1000 (NumPy Variant).

Mathematical Formulation:
Tribonacci meta-exponent recurrence modulo phi(10^9+7) evaluated via NumPy matrix power.
"""

from __future__ import annotations

import numpy as np


def solve(mod: int = 1000000007) -> str:
    """Compute Meta-Problem 1000 answer mod (10^9+7) using NumPy."""
    phi_mod = mod - 1

    M = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0]], dtype=object)
    R = np.eye(3, dtype=object)
    base = M
    p = 1000
    while p > 0:
        if p & 1:
            R = (R @ base) % phi_mod
        base = (base @ base) % phi_mod
        p >>= 1

    exp_val = int(R[0, 0])
    ans = pow(2, exp_val, mod)
    return str(ans)


if __name__ == "__main__":
    print(solve())
