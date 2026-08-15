"""Project Euler 328: Lowest-cost Search

Find sum_{n=1}^{200000} C(n), where C(n) is the minimax search cost for a hidden number in {1, ..., n}.
"""

from __future__ import annotations


def solve(limit: int = 200_000) -> str:
    """Calculates sum_{n=1}^{limit} C(n) using the complete binary right-subtree recurrence:

    C(n) = min_{d >= 1} max( (n - 2^d + 1) + C(n - 2^d), d * n - 2^(d+1) + d + 2 ).
    """
    cost_table = [0] * (limit + 1)

    for n in range(2, limit + 1):
        min_worst_cost = float("inf")
        d = 1
        while (1 << d) - 1 < n:
            k = n - (1 << d) + 1
            cost_left = k + cost_table[k - 1]
            cost_right = d * n - (1 << (d + 1)) + d + 2
            worst_case = max(cost_left, cost_right)
            if worst_case < min_worst_cost:
                min_worst_cost = worst_case
            d += 1
        cost_table[n] = int(min_worst_cost)

    total_sum = sum(cost_table[1:])
    return str(total_sum)


if __name__ == "__main__":
    print(solve())
