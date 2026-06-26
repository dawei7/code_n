"""Optimal solution for fenwick_02: Range Sum Query (BIT).

Build a BIT, apply updates, then answer each range-sum query.
"""


def solve(arr, n, updates, queries, q):
    if n == 0:
        return [0] * q
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = arr[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]

    def update(i, delta):
        i += 1
        while i <= n:
            bit[i] += delta
            i += i & -i

    work = list(arr)
    for idx, val in updates:
        delta = val - work[idx]
        work[idx] = val
        update(idx, delta)

    out = []
    for l, r in queries:
        def prefix(i):
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        out.append(prefix(r) - (prefix(l - 1) if l > 0 else 0))
    return out
