"""Optimal app-local solution for LeetCode 872."""

from itertools import zip_longest


def _leaf_values(root):
    stack = [root] if root is not None else []
    while stack:
        node = stack.pop()
        if node.left is None and node.right is None:
            yield node.val
            continue
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


def solve(root1, root2):
    missing = object()
    return all(
        first == second
        for first, second in zip_longest(
            _leaf_values(root1),
            _leaf_values(root2),
            fillvalue=missing,
        )
    )
