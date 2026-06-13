"""Optimal solution for segtree_03: Point Update.

Apply point updates and return the resulting array.
"""


def solve(arr, n, updates, q):
    work = list(arr)
    for idx, val in updates:
        if 0 <= idx < n:
            work[idx] = val
    return work
