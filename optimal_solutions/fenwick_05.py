"""Optimal solution for fenwick_05: Range Update + Range Query (BIT).

Maintain an array of n integers under repeated
"""


def solve(arr, n, range_updates, range_queries, q):
    """Range add + range sum via two BITs.

    Seed both BITs with the initial arr values so the
    range sum reflects the actual current array.
    """
    INF = n + 5
    bit1 = [0] * (n + 2)
    bit2 = [0] * (n + 2)

    def update(bit, i, delta):
        i += 1
        while i <= n + 1:
            bit[i] += delta
            i += i & -i

    def prefix(bit, i):
        i += 1
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    def range_update(l, r, val):
        update(bit1, l, val)
        if r + 1 < n:
            update(bit1, r + 1, -val)
        update(bit2, l, val * (l - 1))
        if r + 1 < n:
            update(bit2, r + 1, -val * r)

    def prefix_sum(x):
        # sum of [0, x]
        if x < 0:
            return 0
        return prefix(bit1, x) * x - prefix(bit2, x)

    # Initialize: each initial value is a point update (a
    # range update of length 1). This seeds both BITs so the
    # formula (bit1.prefix(x) * x - bit2.prefix(x)) yields
    # sum of arr[0..x] including the initial values.
    for i in range(n):
        range_update(i, i, arr[i])
    for l, r, val in range_updates:
        range_update(l, r, val)
    out = []
    for l, r in range_queries:
        out.append(prefix_sum(r) - prefix_sum(l - 1))
    return out
