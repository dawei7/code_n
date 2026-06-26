"""Optimal solution for suffix_01: Build Suffix Array.

Naive: build all n suffixes and sort them. O(n^2 log n).
"""


def solve(s, n):
    if n == 0:
        return []
    return sorted(range(n), key=lambda i: s[i:])
