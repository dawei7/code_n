"""Optimal solution for LeetCode 1029: Two City Scheduling."""


def solve(costs: list[list[int]]) -> int:
    costs.sort(key=lambda cost: cost[0] - cost[1])
    half = len(costs) // 2
    return sum(cost[0] for cost in costs[:half]) + sum(cost[1] for cost in costs[half:])
