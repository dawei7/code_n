"""Optimal solution for bb_01: 0/1 Knapsack.

Each item is either in the knapsack or not. Recursive choice
with a capacity check. Setup keeps n small (n <= 8) so
exhaustive search is feasible; a real solver would use DP or
branch-and-bound with a fractional-relaxation upper bound.
"""


def solve(values, weights, capacity, n):
    best = 0

    def helper(i, value, weight):
        nonlocal best
        if i == n:
            if value > best:
                best = value
            return
        # Skip item i.
        helper(i + 1, value, weight)
        # Take item i (only if it fits).
        if weight + weights[i] <= capacity:
            helper(i + 1, value + values[i], weight + weights[i])

    helper(0, 0, 0)
    return best
