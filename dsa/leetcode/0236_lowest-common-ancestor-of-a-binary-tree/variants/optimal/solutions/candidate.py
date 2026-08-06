from __future__ import annotations


class TreeNode:
    """Local equivalent of LeetCode's TreeNode for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    stack: list[tuple[TreeNode | None, int, TreeNode | None]] = [(root, 0, None)]
    result = None

    while stack:
        node, state, left = stack.pop()

        if node is None or node is p or node is q:
            result = node
        elif state == 0:
            stack.append((node, 1, None))
            stack.append((node.left, 0, None))
        elif state == 1:
            stack.append((node, 2, result))
            stack.append((node.right, 0, None))
        elif left is not None and result is not None:
            result = node
        elif left is not None:
            result = left

    return result
