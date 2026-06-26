"""Optimal solution for tree_14: Symmetric Tree Check.

Return True iff the binary tree is symmetric around
"""


def solve(children, root, n):
    """True iff the binary tree is a mirror of itself around the root."""
    if root == -1:
        return True

    def is_mirror(a, b):
        if a == -1 and b == -1:
            return True
        if a == -1 or b == -1:
            return False
        return (
            is_mirror(children[a][0], children[b][1])
            and is_mirror(children[a][1], children[b][0])
        )

    return is_mirror(children[root][0], children[root][1])
