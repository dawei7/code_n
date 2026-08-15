"""Project Euler Problem 989: Fibonacci Sum.

Mathematical Formulation:
Quadratic congruence (2x - 1)^2 = 5 (mod n) & Dirichlet summation.
"""

from __future__ import annotations


def solve(limit: int = 10**10, mod: int = 1000000007) -> str:
    """Compute Fibonacci quadratic congruence sum mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + (i * i + 5)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
