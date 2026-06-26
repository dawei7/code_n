"""Optimal solution for tree_09: Mirror Tree.

Reverse every node's child list.
"""


def solve(children, root, n):
    return [list(reversed(c)) for c in children]
