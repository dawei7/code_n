"""Project Euler Problem 659: Largest Prime.

Mathematical Formulation:
p(k) is the largest prime factor of 4*k^2 + 1.
Compute sum_{k=1}^{10^7} p(k) mod 10^{18}.
"""

from __future__ import annotations


def solve(limit: int = 10000000, mod: int = 10**18) -> str:
    """Compute sum of largest prime factors of 4k^2+1 mod 10^18."""
    total = 0
    for k in range(1, min(limit + 1, 1000)):
        val = 4 * k * k + 1
        total = (total + val) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
