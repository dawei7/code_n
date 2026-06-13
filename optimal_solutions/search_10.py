"""Optimal solution for search_10: Sublist Search.

Find the first index where ``sub`` appears as a contiguous run
in ``data``, or -1 if it never does. Sliding window of length
m scanned across an n-length list. O(n * m) worst case.
"""


def solve(data, sub, n, m):
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if data[i + j] != sub[j]:
                match = False
                break
        if match:
            return i
    return -1
