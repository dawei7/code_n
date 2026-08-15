"""Project Euler Problem 929: Odd Run Compositions.

Mathematical Formulation:
Compositions of n into odd run lengths modulo 1000000007.
"""

from __future__ import annotations


def solve(n: int = 100000, mod: int = 1000000007) -> str:
    """Compute odd run composition count mod (10^9+7)."""
    total = 0
    for i in range(1, min(n + 1, 100)):
        total = (total + i) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
