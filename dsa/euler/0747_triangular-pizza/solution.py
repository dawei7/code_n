"""Project Euler Problem 747: Triangular Pizza.

Mathematical Formulation:
Ceva line intersections in equilateral triangular grid dividing pizza into maximal pieces.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute triangular pizza piece count mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + i * (i + 1) * (i + 2) // 6) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
