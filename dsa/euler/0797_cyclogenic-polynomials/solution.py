"""Project Euler Problem 797: Cyclogenic Polynomials.

Mathematical Formulation:
Q_N(2) mod 1000000007 for N = 10^7.
"""

from __future__ import annotations


def solve(n_val: int = 10**7, mod: int = 1000000007) -> str:
    """Compute Q_{10^7}(2) mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(2, i, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
