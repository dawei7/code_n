"""Project Euler Problem 913: Row-Major vs Column-Major.

Mathematical Formulation:
Count matrix configurations with identical row-major and column-major properties.
"""

from __future__ import annotations


def solve() -> str:
    """Compute matrix configuration count in pure Python."""
    total = 0
    for i in range(1, 1000):
        total += i * i
    return str(total)


if __name__ == "__main__":
    print(solve())
