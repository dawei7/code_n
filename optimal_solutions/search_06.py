"""Optimal solution for search_06: Jump Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(log n) time.
"""


def solve(data, target, n):
    import math
    step = max(1, int(math.sqrt(n)))
    prev = 0
    # Find the block where the target could be.
    while prev < n and data[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    # Linear scan inside the block.
    for index in range(prev, min(step, n)):
        if data[index] == target:
            return index
    return -1
