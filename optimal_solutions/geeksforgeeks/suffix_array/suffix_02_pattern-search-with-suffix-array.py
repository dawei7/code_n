"""Optimal solution for suffix_02: Pattern Search with Suffix Array.

Build SA, then binary-search for the range of suffixes
that start with pattern.
"""


def solve(s, n, pattern, m):
    if m == 0 or n == 0:
        return []
    sa = sorted(range(n), key=lambda i: s[i:])
    out = []
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if s[sa[mid]:] < pattern:
            lo = mid + 1
        else:
            hi = mid
    lower = lo
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        if s[sa[mid]:].startswith(pattern):
            lo = mid + 1
        elif s[sa[mid]:] < pattern:
            lo = mid + 1
        else:
            hi = mid
    upper = lo
    for i in range(lower, upper):
        out.append(sa[i])
    return sorted(out)
