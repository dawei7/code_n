"""Optimal solution for search_12: Search in Rotated Sorted Array.

A sorted array that has been rotated at some unknown pivot.
Find the index of ``target`` (or -1) in O(log n) time.
Find the pivot (smallest element) first, then binary-search
the half that could contain the target.
"""


def solve(data, target, n):
    if n == 0:
        return -1
    low, high = 0, n - 1
    # Find the rotation pivot: the smallest element.
    while low < high:
        mid = (low + high) // 2
        if data[mid] > data[high]:
            low = mid + 1
        else:
            high = mid
    pivot = low
    # Decide which half to search.
    if pivot == 0:
        low, high = 0, n - 1
    elif data[0] <= target <= data[pivot - 1]:
        # Target is in the upper half (data[0..pivot-1]).
        low, high = 0, pivot - 1
    else:
        # Target is in the lower half (data[pivot..n-1]).
        low, high = pivot, n - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
