"""Optimal solution for string_07: Z-Algorithm.

Linear-time pattern matching.
"""


def solve(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    s = pattern + "$" + text
    z = [0] * len(s)
    l = 0
    r = 0
    for i in range(1, len(s)):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    offset = m + 1
    for i in range(offset, len(s)):
        if z[i] == m:
            return i - offset
    return -1
