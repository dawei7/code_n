"""Project Euler Problem 726: Falling Bottles.

Mathematical Formulation:
F(n, k) counts configurations of n rows of collapsing bottles after k removals.
"""

from __future__ import annotations


def solve(n: int = 10000, mod: int = 1000000007) -> str:
    """Compute falling bottle configuration count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i * (i + 1) // 2) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
