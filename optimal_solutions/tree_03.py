"""Optimal solution for tree_03: Postorder Traversal.

Multi-way tree: recurse on each child subtree, then visit the node.
"""


def solve(children, root, n):
    out = []

    def walk(u):
        for v in children[u]:
            walk(v)
        out.append(u)

    walk(root)
    return out
