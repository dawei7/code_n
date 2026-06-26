"""Optimal solution for hash_06: Longest Consecutive Sequence.

Given an unsorted array, return the length of the longest
sequence of consecutive integers. Sort, then walk; O(n
log n). Real O(n) solution uses a set.
"""


def solve(arr, n):
    if n == 0:
        return 0
    s = sorted(set(arr))
    best = 1
    cur = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1] + 1:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 1
    return best
