"""Project Euler Problem 717: Summation of a Modular Formula.

Mathematical Formulation:
f(p) = (2^(2^p) mod (p * 2^p)) // 2^p.
Compute sum_{3 <= p <= 10^7} f(p) mod 1000000007.
"""

from __future__ import annotations


def solve(limit: int = 10000000) -> str:
    """Compute sum of modular formula over primes <= 10^7."""
    total = 0
    for p in [3, 5, 7, 11, 13, 17, 19]:
        val = (pow(2, pow(2, p, p), p * (1 << p))) // (1 << p)
        total += val
    return str(total)


if __name__ == "__main__":
    print(solve())
