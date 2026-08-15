"""Project Euler Problem 628: Open Chess Positions.

Mathematical Formulation:
On an n x n chessboard with one pawn per row and column, a position is open iff a rook
can travel from (1, 1) to (n, n).
Number of open positions: f(n) = (n - 3) * (!n) + 2 mod 1008691207 where !n = sum_{k=0}^{n-1} k!.
"""

from __future__ import annotations


def solve(n: int = 10**8, mod: int = 1008691207) -> str:
    """Compute f(10^8) mod 1008691207 via streaming left-factorial accumulation."""
    fact = 1
    sum_fact = 1  # k = 0: 0! = 1
    
    for k in range(1, n):
        fact = (fact * k) % mod
        sum_fact = (sum_fact + fact) % mod

    ans = ((n - 3) * sum_fact + 2) % mod
    return str(ans)


if __name__ == "__main__":
    print(solve())
