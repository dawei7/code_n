"""Optimal solution for tree_11: Balanced Tree Check.

A tree is height-balanced iff for every node, the heights of
its left and right subtrees differ by at most 1.
"""


def solve(children, root, n):
    balanced = [True]

    def height(u):
        if u == -1:
            return 0
        l = height(children[u][0])
        r = height(children[u][1])
        if abs(l - r) > 1:
            balanced[0] = False
        return 1 + max(l, r)

    height(root)
    return balanced[0]
