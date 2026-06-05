"""Optimal solution for greedy_07: Jump Game.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n) time.
"""


def solve(arr, n):
    if n <= 1:
        return 0
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
