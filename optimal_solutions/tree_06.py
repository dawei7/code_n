"""Optimal solution for tree_06: BST Search.

Walk a binary search tree, comparing the target to each node's
value, going left or right accordingly.
"""


def solve(children, values, root, n, target):
    u = root
    while u is not None and u != -1:
        if values[u] == target:
            return u
        left, right = children[u]
        if target < values[u]:
            u = left if left != -1 else None
        else:
            u = right if right != -1 else None
    return -1
