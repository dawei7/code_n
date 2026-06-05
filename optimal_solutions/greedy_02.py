"""Optimal solution for greedy_02: Fractional Knapsack.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(values, weights, capacity, n):
    # Sort items by value-to-weight ratio (descending). Pair indices
    # so we can sort on the ratio without losing the alignment.
    order = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    remaining = capacity
    total = 0.0
    for index in order:
        w = weights[index]
        if remaining >= w:
            total += values[index]
            remaining -= w
        else:
            total += values[index] * (remaining / w)
            break
    return total
