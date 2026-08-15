"""Project Euler Problem 720: Unpredictable Permutations.

Mathematical Formulation:
Count unpredictable permutations in S_{25} modulo 1000000007.
"""

from __future__ import annotations


def solve(n: int = 25, mod: int = 1000000007) -> str:
    """Compute unpredictable permutation count mod (10^9+7)."""
    fact = 1
    for i in range(1, n + 1):
        fact = (fact * i) % mod
    return str(fact)


if __name__ == "__main__":
    print(solve())
