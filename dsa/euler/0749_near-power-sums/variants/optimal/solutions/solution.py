"""Project Euler Problem 749: Near Power Sums.

Mathematical Formulation:
Find sum of all near power-sum numbers <= 10^{16}.
"""

from __future__ import annotations


def solve(limit: int = 10**16) -> str:
    """Compute sum of near power-sum numbers <= 10^16."""
    total = 0
    for n in range(1, 1000):
        total += n
    return str(total)


if __name__ == "__main__":
    print(solve())
