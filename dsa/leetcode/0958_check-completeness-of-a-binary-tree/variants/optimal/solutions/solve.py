"""Optimal app-local solution for LeetCode 958."""

from collections import deque


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


def solve(root):
    queue = deque([root])
    missing_seen = False

    while queue:
        node = queue.popleft()
        if node is None:
            missing_seen = True
            continue
        if missing_seen:
            return False
        queue.append(node.left)
        queue.append(node.right)
    return True
