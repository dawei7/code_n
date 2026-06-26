"""Optimal solution for search_05: Ternary Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(log n) time.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high:
        third = (high - low) // 3
        mid1 = low + third
        mid2 = high - third
        if data[mid1] == target:
            return mid1
        if data[mid2] == target:
            return mid2
        if target < data[mid1]:
            high = mid1 - 1
        elif target > data[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1
