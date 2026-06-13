"""Optimal solution for segtree_04: Range Minimum Query.

Build a min-segment tree on arr (each node stores
"""


def solve(arr, n, queries, q):
    """Range Minimum Query via segment tree."""
    if n == 0:
        return [0] * q
    tree = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
        else:
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return float("inf")
        if l <= lo and hi <= r:
            return tree[node]
        mid = (lo + hi) // 2
        return min(query(2 * node, lo, mid, l, r),
                   query(2 * node + 1, mid + 1, hi, l, r))

    build(1, 0, n - 1)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
