"""Optimal solution for dp_07: Longest Increasing Subsequence.

Patience sorting with binary search — O(n log n).
"""


def solve(arr):
    import bisect
    tails = []
    for v in arr:
        i = bisect.bisect_left(tails, v)
        if i == len(tails):
            tails.append(v)
        else:
            tails[i] = v
    return len(tails)
