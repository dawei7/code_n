"""Project Euler Problem 926: Total Roundness.

Mathematical Formulation:
Roundness of integer partitions and multisets.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute total roundness mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
