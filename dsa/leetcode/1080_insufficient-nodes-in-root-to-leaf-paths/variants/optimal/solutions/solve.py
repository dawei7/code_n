"""Optimal solution for LeetCode 1080: Insufficient Nodes in Root to Leaf Paths."""

from typing import Any


class TreeNode:
    """Local equivalent of LeetCode's TreeNode for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Any | None, limit: int) -> Any | None:
    if root is None:
        return None

    stack = [(root, None, "", limit, False, False)]
    while stack:
        node, parent, side, need, expanded, was_leaf = stack.pop()
        if not expanded:
            was_leaf = node.left is None and node.right is None
            stack.append((node, parent, side, need, True, was_leaf))
            child_need = need - node.val
            if node.right is not None:
                stack.append((node.right, node, "right", child_need, False, False))
            if node.left is not None:
                stack.append((node.left, node, "left", child_need, False, False))
            continue

        survives = node.val >= need if was_leaf else node.left is not None or node.right is not None
        if not survives:
            if parent is None:
                root = None
            else:
                setattr(parent, side, None)

    return root
