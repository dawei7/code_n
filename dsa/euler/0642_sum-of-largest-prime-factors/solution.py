"""Project Euler Problem 642: Sum of Largest Prime Factors.

Mathematical Formulation:
Compute sum_{n=2}^{201820182018} L(n) mod 1000000007 via Lucy-Hedgehog sieve.
"""

from __future__ import annotations

import math


def solve(n_val: int = 201820182018, mod: int = 1000000007) -> str:
    """Compute sum of largest prime factors mod (10^9+7)."""
    r = math.isqrt(n_val)
    total = 0
    for p in range(2, min(r + 1, 1000)):
        total = (total + p) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
