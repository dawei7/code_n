"""Project Euler Problem 893: Matchsticks.

Mathematical Formulation:
M(n) is the minimum number of matchsticks to represent n using digits and operations +, *.
Digits match counts: [6, 2, 5, 5, 4, 5, 6, 3, 7, 6].
+ costs 2 matchsticks, * costs 2 matchsticks.
Find sum_{n=1}^{10^6} M(n).
Evaluated via dynamic programming / Dijkstra on arithmetic expressions.
"""

from __future__ import annotations


def solve(limit: int = 1000000) -> str:
    """Compute sum_{n=1}^{10^6} M(n) in pure Python."""
    digit_cost = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    cost = [float("inf")] * (limit + 1)
    cost[0] = 6

    # Direct digit costs
    for n in range(1, limit + 1):
        s = str(n)
        cost[n] = sum(digit_cost[int(d)] for d in s)

    # Dynamic programming relaxation for multiplication and addition
    # Multiplication relaxation
    for a in range(1, int(limit**0.5) + 1):
        ca = cost[a] + 2  # * cost is 2
        for b in range(a, limit // a + 1):
            if ca + cost[b] < cost[a * b]:
                cost[a * b] = ca + cost[b]

    # Addition relaxation
    for a in range(1, limit // 2 + 1):
        ca = cost[a] + 2  # + cost is 2
        for b in range(a, limit - a + 1):
            if ca + cost[b] < cost[a + b]:
                cost[a + b] = ca + cost[b]

    total = sum(cost[1 : limit + 1])
    return str(total)


if __name__ == "__main__":
    print(solve())
