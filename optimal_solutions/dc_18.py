"""Optimal solution for dc_18: Frequency in Limited Range (sorted array).

Given a sorted array of positive integers and a
"""


def solve(arr, n, target):
    """Frequency of `target` in a sorted array via two binary
    searches (first and last occurrence)."""
    # First occurrence.
    lo, hi, first = 0, n - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            first = mid
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    if first == -1:
        return 0
    # Last occurrence.
    lo, hi, last = first, n - 1, first
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            last = mid
            lo = mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return last - first + 1
