"""Optimal solution for suffix_03: LCP Array (Kasai's Algorithm).

Given a string s, return its suffix array sa and
"""


def solve(s, n):
    """Return (suffix_array, lcp_array) of s.

    Build the suffix array naively (sort suffixes), then run
    Kasai's algorithm to build the LCP array in O(n).
    """
    if n == 0:
        return [], []
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Inverse SA: rank[i] = position of suffix i in sa.
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    # Kasai's algorithm.
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            # j is the previous suffix in the suffix array.
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
        # If rank[i] == 0 (it's the smallest suffix), lcp[0] = 0
        # (already initialized).
    return sa, lcp
