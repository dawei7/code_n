"""Optimal solution for segtree_05: Range Update with Lazy Propagation.

Build a sum-segment tree, then apply a sequence
"""


def solve(arr, n, range_updates, queries, q):
    """Sum-segment tree with lazy-propagation range updates."""
    if n == 0:
        return [0] * q
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
            return
        mid = (lo + hi) // 2
        build(2 * node, lo, mid)
        build(2 * node + 1, mid + 1, hi)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def apply(node, lo, hi, val):
        """Apply a pending update of `val` to this node."""
        tree[node] += val * (hi - lo + 1)
        lazy[node] += val

    def push(node, lo, hi):
        """Push pending lazy update down to children."""
        if lazy[node] != 0 and lo != hi:
            mid = (lo + hi) // 2
            apply(2 * node, lo, mid, lazy[node])
            apply(2 * node + 1, mid + 1, hi, lazy[node])
            lazy[node] = 0

    def update(node, lo, hi, l, r, val):
        if l > hi or r < lo:
            return
        if l <= lo and hi <= r:
            apply(node, lo, hi, val)
            return
        push(node, lo, hi)
        mid = (lo + hi) // 2
        update(2 * node, lo, mid, l, r, val)
        update(2 * node + 1, mid + 1, hi, l, r, val)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return 0
        if l <= lo and hi <= r:
            return tree[node]
        push(node, lo, hi)
        mid = (lo + hi) // 2
        return query(2 * node, lo, mid, l, r) + query(2 * node + 1, mid + 1, hi, l, r)

    build(1, 0, n - 1)
    for l, r, val in range_updates:
        update(1, 0, n - 1, l, r, val)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
