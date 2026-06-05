"""Optimal solution for search_02: Binary Search.

Sorted array; halve the search space each step. O(log n) time.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        value = data[mid]
        if value == target:
            return mid
        if value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
