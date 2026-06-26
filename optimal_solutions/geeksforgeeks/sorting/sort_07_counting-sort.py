"""Optimal solution for sort_07: Counting Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n) time.
"""


def solve(data, n):
    if n == 0:
        return data
    min_val = min(data)
    max_val = max(data)
    span = max_val - min_val + 1
    counts = [0] * span
    for value in data:
        counts[value - min_val] += 1
    # Rewrite data in place by walking the count array.
    index = 0
    for offset, count in enumerate(counts):
        for _ in range(count):
            data[index] = offset + min_val
            index += 1
    return data
