"""Optimal solution for tree_04: Tree Height.

A leaf has height 0; a non-leaf has height 1 + max(child height).
"""


def solve(children, root, n):
    def depth(u):
        if not children[u]:
            return 0
        return 1 + max(depth(v) for v in children[u])
    return depth(root)
