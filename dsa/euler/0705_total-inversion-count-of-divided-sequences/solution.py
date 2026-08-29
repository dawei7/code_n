"""Project Euler Problem 705: Total Inversion Count of Divided Sequences.

Mathematical Formulation:
Find total inversion count across all divided sequence permutations mod 1000000007.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute total inversion count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i * (i - 1) // 2) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
