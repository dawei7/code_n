"""Optimal solution for greedy_10: Minimum Coins.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(coins, amount):
    count = 0
    for c in sorted(coins, reverse=True):
        if c <= 0:
            continue
        while amount >= c:
            amount -= c
            count += 1
        if amount == 0:
            break
    if amount == 0:
        return count
    return -1
