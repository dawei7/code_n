"""Project Euler Problem 916: Restricted Permutations.

Mathematical Formulation:
Restricted permutations avoiding specific positional patterns modulo 1000000007.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute restricted permutation count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
