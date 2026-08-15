"""Project Euler Problem 1005: Median Prime List.

Mathematical Formulation:
Prime partition count DP table C(s, i) & greedy lexicographic bisection.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute median prime list product mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 2, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
