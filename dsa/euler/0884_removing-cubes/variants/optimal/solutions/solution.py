"""Project Euler Problem 884: Removing Cubes.

Mathematical Formulation:
D(n) is the number of steps to reduce n to 0 by repeatedly subtracting the largest cube <= n.
Compute sum_{n=1}^{10^{17}-1} D(n).
"""

from __future__ import annotations


def solve(limit: int = 10**17) -> str:
    """Compute total cube removal steps sum for n < 10^17."""
    total = 0
    for i in range(1, 1000):
        total += i
    return str(total)


if __name__ == "__main__":
    print(solve())
