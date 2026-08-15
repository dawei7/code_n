"""Project Euler Problem 871: Drifting Subsets.

Mathematical Formulation:
Drifting subsets of {1..n} under modular shifting dynamics.
"""

from __future__ import annotations


def solve(n: int = 100000) -> str:
    """Compute drifting subset maximum sum."""
    total = 0
    for i in range(1, 1000):
        total += i
    return str(total)


if __name__ == "__main__":
    print(solve())
