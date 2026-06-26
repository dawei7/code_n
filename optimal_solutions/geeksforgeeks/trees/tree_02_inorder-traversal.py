"""Optimal solution for tree_02: Inorder Traversal.

Multi-way tree: first-child subtree, then the node, then each
remaining child subtree left-to-right.
"""


def solve(children, root, n):
    out = []

    def walk(u):
        if children[u]:
            walk(children[u][0])
        out.append(u)
        for v in children[u][1:]:
            walk(v)

    walk(root)
    return out
