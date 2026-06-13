"""Optimal solution for dc_17: Min and Max (D&C tournament).

Given an array of n integers, return the minimum
"""


def solve(arr, n):
    """D&C tournament min/max. Returns [lo, hi]."""
    def rec(lo, hi):
        if lo == hi:
            return [arr[lo], arr[lo]]
        if hi == lo + 1:
            if arr[lo] < arr[hi]:
                return [arr[lo], arr[hi]]
            return [arr[hi], arr[lo]]
        mid = (lo + hi) // 2
        a = rec(lo, mid)
        b = rec(mid + 1, hi)
        return [min(a[0], b[0]), max(a[1], b[1])]
    return rec(0, n - 1)
