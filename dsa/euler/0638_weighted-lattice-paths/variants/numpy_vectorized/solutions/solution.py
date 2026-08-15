"""Project Euler Problem 638: Weighted Lattice Paths (NumPy Vectorized Variant).

Mathematical Formulation:
C(a, b, k) = sum_{P} k^{Area(P)} = [a+b, a]_k (Gaussian q-binomial coefficient).
Evaluated using vectorized NumPy modular array operations.
"""

from __future__ import annotations

import numpy as np


def q_binomial_np(n: int, k: int, q: int, mod: int = 1000000007) -> int:
    """Compute Gaussian q-binomial coefficient using vectorized modular operations."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if q == 1:
        # Standard binomial coefficient
        num_arr = np.arange(n - k + 1, n + 1, dtype=object)
        den_arr = np.arange(1, k + 1, dtype=object)
        num = int(np.prod(num_arr % mod) % mod)
        den = int(np.prod(den_arr % mod) % mod)
        return (num * pow(den, mod - 2, mod)) % mod

    # For q >= 2:
    j = np.arange(1, k + 1, dtype=object)
    # Exponent array
    exp_num = (n - j + 1).tolist()
    exp_den = j.tolist()
    
    num = 1
    den = 1
    for en, ed in zip(exp_num, exp_den):
        num = (num * (pow(q, en, mod) - 1)) % mod
        den = (den * (pow(q, ed, mod) - 1)) % mod

    return (num * pow(den, mod - 2, mod)) % mod


def solve(mod: int = 1000000007) -> str:
    """Compute sum_{k=1}^7 C(10^k + k, 10^k + k, k) mod mod with NumPy."""
    total = 0
    for k in range(1, 8):
        n = 10**k + k
        val = q_binomial_np(2 * n, n, k, mod)
        total = (total + val) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
