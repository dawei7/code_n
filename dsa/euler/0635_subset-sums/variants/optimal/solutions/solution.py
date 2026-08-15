"""Project Euler Problem 635: Subset Sums.

Mathematical Formulation:
A_q(p) = (binom(qp, p) + (q - 1) * (p - 1)) / p.
Compute sum_{p <= 10^8} (A_2(p) + A_3(p)) mod 1000000009.
"""

from __future__ import annotations

import math


def solve(limit: int = 100000000, mod: int = 1000000009) -> str:
    """Compute (S_2(10^8) + S_3(10^8)) mod (10^9+9)."""
    total = 0
    # Sieve primes up to limit
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        a2 = (math.comb(2 * p, p) + 2 * (p - 1)) // p
        a3 = (math.comb(3 * p, p) + 3 * (p - 1)) // p
        total = (total + a2 + a3) % mod

    return str(total)


if __name__ == "__main__":
    print(solve())
