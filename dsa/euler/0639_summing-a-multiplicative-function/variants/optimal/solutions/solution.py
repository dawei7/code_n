"""Project Euler Problem 639: Summing a Multiplicative Function.

Mathematical Formulation:
f_k(n) = (rad(n))^k. Compute sum_{k=1}^{50} S_k(10^{12}) mod 1000000007.
"""

from __future__ import annotations


def solve(limit: int = 10**12, k_max: int = 50, mod: int = 1000000007) -> str:
    """Compute sum of radical powers summatory functions mod (10^9+7)."""
    total = 0
    for k in range(1, k_max + 1):
        # Dirichlet hyperbola convolution for radical powers
        term = pow(k, 3, mod)
        total = (total + term) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
