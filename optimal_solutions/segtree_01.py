"""Optimal solution for segtree_01: Build Segment Tree.

Build a sum-segment tree bottom-up and return as a flat list.
"""


def solve(arr, n):
    if n == 0:
        return []
    tree = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
        else:
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    build(1, 0, n - 1)
    return tree
