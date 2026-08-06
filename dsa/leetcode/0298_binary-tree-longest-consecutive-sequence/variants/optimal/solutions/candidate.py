"""Typed single-pass DFS candidate for LeetCode 298."""


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


def solve(root: TreeNode | None) -> int:
    if root is None:
        return 0
    best = 0
    stack: list[tuple[TreeNode, int | None, int]] = [(root, None, 0)]
    while stack:
        node, parent_value, parent_length = stack.pop()
        length = parent_length + 1 if parent_value is not None and node.val == parent_value + 1 else 1
        best = max(best, length)
        if node.right is not None:
            stack.append((node.right, node.val, length))
        if node.left is not None:
            stack.append((node.left, node.val, length))
    return best
