"""Optimal solution for string_13: Z-Algorithm (Pattern Search).

Build the Z-array of pattern + '$' + s, then collect
positions where Z[i] == |pattern| in the s region.
"""


def solve(s, n, pattern, m):
    if m == 0 or n == 0:
        return []
    combined = pattern + "$" + s
    L = len(combined)
    z = [0] * L
    left = 0
    right = 0
    for i in range(1, L):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < L and combined[z[i]] == combined[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    out = []
    for i in range(m + 1, L):
        if z[i] == m:
            out.append(i - m - 1)
    return out
