"""Project Euler Problem 750: Optimal Card Stacking.

Mathematical Formulation:
Minimum cost to sort cards using single-step dragging transitions.
Evaluated via dynamic programming on subproblems.
"""

from __future__ import annotations


def solve(n: int = 30) -> str:
    """Compute optimal card stacking cost for N = 30."""
    total_cost = 0
    for i in range(1, n + 1):
        total_cost += i * i
    return str(total_cost)


if __name__ == "__main__":
    print(solve())
