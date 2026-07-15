"""Optimal app-local solution for LeetCode 998."""


def solve(root, val):
    node_type = type(root)
    inserted = node_type(val)

    if val > root.val:
        inserted.left = root
        return inserted

    current = root
    while current.right is not None and current.right.val > val:
        current = current.right

    inserted.left = current.right
    current.right = inserted
    return root
