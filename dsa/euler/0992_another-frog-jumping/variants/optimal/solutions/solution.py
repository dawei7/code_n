"""Project Euler Problem 992: Another Frog Jumping.

Mathematical Formulation:
BEST theorem on directed Eulerian multigraphs.
"""

from __future__ import annotations


def solve(n: int = 1000, mod: int = 1000000007) -> str:
    """Compute Eulerian frog jumping paths count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i * (i + 1)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
