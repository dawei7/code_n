"""Optimal app-local solution for LeetCode 1325."""


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


def solve(root, target):
    result = root
    stack = [(root, None, None, False)]
    while stack:
        node, parent, side, visited = stack.pop()
        if not visited:
            stack.append((node, parent, side, True))
            if node.right is not None:
                stack.append((node.right, node, "right", False))
            if node.left is not None:
                stack.append((node.left, node, "left", False))
            continue

        if node.left is None and node.right is None and node.val == target:
            if parent is None:
                result = None
            else:
                setattr(parent, side, None)
    return result
