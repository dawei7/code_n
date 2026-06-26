"""Optimal solution for search_07: Exponential Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(log n) time.
"""


def solve(data, target, n):
    if n == 0 or data[0] > target:
        return -1
    bound = 1
    while bound < n and data[bound] <= target:
        bound *= 2
    # Binary search in [bound/2, min(bound, n-1)].
    low, high = bound // 2, min(bound, n - 1)
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
