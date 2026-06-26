"""Optimal solution for tree_01: Preorder Traversal.

Multi-way tree: children[i] is the list of i's children. Visit
the node, then recurse on each child left-to-right.
"""


def solve(children, root, n):
    out = []

    def walk(u):
        out.append(u)
        for v in children[u]:
            walk(v)

    walk(root)
    return out
