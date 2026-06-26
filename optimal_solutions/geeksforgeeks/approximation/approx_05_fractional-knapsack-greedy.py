"""Optimal solution for approx_05: Fractional Knapsack (Greedy).

Given n items each with a value and a weight, and a
"""


def solve(values, weights, n, capacity):
    """Fractional knapsack via greedy by value/weight ratio."""
    if capacity <= 0 or n == 0:
        return 0.0
    items = sorted(
        range(n),
        key=lambda i: values[i] / weights[i],
        reverse=True,
    )
    remaining = capacity
    total = 0.0
    for i in items:
        if remaining <= 0:
            break
        if weights[i] <= remaining:
            total += values[i]
            remaining -= weights[i]
        else:
            total += values[i] * (remaining / weights[i])
            remaining = 0
    return total
