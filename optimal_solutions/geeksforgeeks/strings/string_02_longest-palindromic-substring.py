"""Optimal solution for string_02: Longest Palindromic Substring.

Expand around every center, track the longest palindrome, return
the leftmost on tie.
"""


def solve(s):
    n = len(s)
    if n == 0:
        return ""
    best_lo, best_hi = 0, 0

    def expand(lo, hi):
        while lo >= 0 and hi < n and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return lo + 1, hi - 1

    for c in range(n):
        lo, hi = expand(c, c)
        if hi - lo > best_hi - best_lo:
            best_lo, best_hi = lo, hi
        if c > 0:
            lo, hi = expand(c - 1, c)
            if hi - lo > best_hi - best_lo:
                best_lo, best_hi = lo, hi

    return s[best_lo:best_hi + 1]
