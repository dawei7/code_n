"""Optimal app-local solution for LeetCode 1029."""


def solve(costs):
    ordered = sorted(costs, key=lambda cost: cost[0] - cost[1])
    half = len(ordered) // 2
    return sum(cost[0] for cost in ordered[:half]) + sum(
        cost[1] for cost in ordered[half:]
    )
