"""Optimal solution for randomized_04: Randomized Binary Search.

Given a sorted list of n distinct integers and a
"""


def solve(arr, n, target):
    """Randomized binary search.

    Pick a uniformly random pivot in [lo, hi], then narrow
    the range based on whether arr[pivot] is less than,
    greater than, or equal to target. Expected O(log n).
    """
    import random
    if n == 0:
        return -1
    lo, hi = 0, n - 1
    while lo <= hi:
        pivot = random.randint(lo, hi)
        if arr[pivot] == target:
            return pivot
        if arr[pivot] < target:
            lo = pivot + 1
        else:
            hi = pivot - 1
    return -1
