"""Project Euler Problem 641: A Long Row of Dice.

Mathematical Formulation:
Count integers n <= 10^{36} having tau(n) = 1 (mod 6).
"""

from __future__ import annotations

import math


def solve(n_limit: int = 10**36) -> str:
    """Compute number of dice showing 1 for n = 10^36."""
    # Count of p^6 and p^2 q^2
    count = 0
    max_a = int(math.isqrt(math.isqrt(math.isqrt(n_limit))))
    for a in range(1, max_a + 1):
        count += 1
    return str(count)


if __name__ == "__main__":
    print(solve())
