"""Optimal solution for greedy_06: Gas Station.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n) time.
"""


def solve(gas, cost, n):
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    start = 0
    for i in range(n):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start
