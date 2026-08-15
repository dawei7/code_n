"""Project Euler Problem 721: High Powers of Irrational Numbers (NumPy Variant).

Mathematical Formulation:
f(a, n) = floor((ceil(sqrt(a)) + sqrt(a))^n).
Evaluated using NumPy 2x2 modular matrix multiplication.
"""

from __future__ import annotations

import math
import numpy as np


def mat_pow_mod_np(P: int, Q: int, exp: int, mod: int) -> int:
    """Compute u_n trace using NumPy 2x2 modular matrix exponentiation."""
    M = np.array([[P % mod, (-Q) % mod], [1, 0]], dtype=object)
    R = np.eye(2, dtype=object)
    base = M
    while exp > 0:
        if exp & 1:
            R = (R @ base) % mod
        base = (base @ base) % mod
        exp >>= 1

    u_n = int((R[0, 0] * P + R[0, 1] * 2) % mod)
    return u_n


def solve(n_limit: int = 5000000, mod: int = 999999937) -> str:
    """Compute G(N) mod 999999937 using NumPy matrix routines."""
    total = 0
    for a in range(1, n_limit + 1):
        c = math.isqrt(a)
        if c * c < a:
            c += 1
        n = a * a
        if a == c * c:
            val = pow(2 * c, n, mod)
        else:
            P = 2 * c
            Q = c * c - a
            u_n = mat_pow_mod_np(P, Q, n - 1, mod)
            val = (u_n - 1) % mod
        total = (total + val) % mod

    return str(total % mod)


if __name__ == "__main__":
    print(solve())
