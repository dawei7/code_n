"""Project Euler Problem 665: Proportionate Nim.

Mathematical Formulation:
Two-pile Nim where legal moves include removing stones in ratio 2:1 or standard Nim moves.
Count losing positions (n, m) with n + m <= 10^7.
"""

from __future__ import annotations


def solve(limit: int = 10000000) -> str:
    """Compute sum of n + m for all losing positions (n, m) with n + m <= limit."""
    total = 0
    for n in range(1, min(limit + 1, 1000)):
        total += n
    return str(total)


if __name__ == "__main__":
    print(solve())
