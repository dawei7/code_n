"""Optimal solution for fenwick_04: Range Update + Point Query (BIT).

Maintain an array of n integers under repeated
"""


def solve(arr, n, range_updates, point_queries, q):
    """Range add + point query via single BIT.

    Seed the BIT with the initial arr values (so the point
    query at idx returns arr[idx] + accumulated deltas).
    """
    bit = [0] * (n + 2)

    def update(i, delta):
        i += 1
        while i <= n + 1:
            bit[i] += delta
            i += i & -i

    def prefix(i):
        i += 1
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    # Initialize the BIT with the DIFF array, not the values.
    # For the "range update, point query" technique, the BIT
    # stores a difference array so that point query at idx
    # gives the current value at idx.
    if n > 0:
        update(0, arr[0])
        for i in range(1, n):
            update(i, arr[i] - arr[i - 1])
    # Apply range updates: diff array approach.
    for l, r, val in range_updates:
        update(l, val)
        if r + 1 < n:
            update(r + 1, -val)
    # Point queries: read prefix sum at each index.
    out = []
    for (idx,) in point_queries:
        out.append(prefix(idx))
    return out
