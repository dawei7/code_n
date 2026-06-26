"""Optimal solution for suffix_04: Count Distinct Substrings.

Count the number of distinct non-empty substrings
"""


def solve(s, n):
    """Count distinct non-empty substrings via suffix array."""
    if n == 0:
        return 0
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Build the LCP array (Kasai-style, but the naive
    # version suffices for small n).
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    # Sum of (n - sa[i] - lcp[i]) for i in 0..n-1.
    total = 0
    for i in range(n):
        total += n - sa[i] - lcp[i]
    return total
