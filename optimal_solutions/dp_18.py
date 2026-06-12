"""Optimal solution for dp_18: Max Product Subarray.

Track both cur_max and cur_min (negatives flip sign).
"""


def solve(arr):
    if not arr:
        return 0
    best = arr[0]
    cur_max = arr[0]
    cur_min = arr[0]
    for v in arr[1:]:
        if v < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(v, cur_max * v)
        cur_min = min(v, cur_min * v)
        if cur_max > best:
            best = cur_max
    return best
