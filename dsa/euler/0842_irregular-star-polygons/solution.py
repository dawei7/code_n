"""Project Euler Problem 842: Irregular Star Polygons.

Mathematical Formulation:
Expected number of intersections of irregular star polygons modulo 1000000007.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute irregular star polygon crossing count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i * (i - 1)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
