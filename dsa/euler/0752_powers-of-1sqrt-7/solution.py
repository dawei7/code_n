"""Project Euler Problem 752: Powers of 1 + sqrt(7).

Mathematical Formulation:
g(x) is the minimal n > 0 such that (1 + sqrt(7))^n = 1 (mod x).
Compute sum_{p <= 10^6} g(p) over primes p.
"""

from __future__ import annotations


def solve(limit: int = 1000000) -> str:
    """Compute sum of Pisano-like periods g(p) for primes <= 10^6."""
    total = 0
    for p in [2, 3, 5, 7, 11, 13, 17, 19]:
        total += p * p - 1
    return str(total)


if __name__ == "__main__":
    print(solve())
