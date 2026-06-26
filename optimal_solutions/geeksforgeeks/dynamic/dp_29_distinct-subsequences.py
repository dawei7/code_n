"""Optimal solution for dp_29: LIS (Patience Sort).

Maintain a sorted tails array; binary-search to place each
value. O(n log n).
"""


def solve(arr, n):
    if n == 0:
        return 0
    import bisect
    tails = []
    for v in arr:
        idx = bisect.bisect_left(tails, v)
        if idx == len(tails):
            tails.append(v)
        else:
            tails[idx] = v
    return len(tails)
