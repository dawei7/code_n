"""Optimal solution for dc_13: Allocate Minimum Number of Pages.

Given an array arr[] of n book page counts and m
"""


def solve(arr, n, m):
    """Binary search on the answer.

    Low = max(arr) (one student reads the longest book alone).
    High = sum(arr) (one student reads everything).
    The first `mx` for which we can split into <= m blocks
    is the answer.
    """
    lo = max(arr) if arr else 0
    hi = sum(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        # Greedy: how many students do we need for max = mid?
        needed = 1
        pages = 0
        for pages_i in arr:
            if pages + pages_i <= mid:
                pages += pages_i
            else:
                needed += 1
                pages = pages_i
        if needed <= m:
            hi = mid
        else:
            lo = mid + 1
    return lo
