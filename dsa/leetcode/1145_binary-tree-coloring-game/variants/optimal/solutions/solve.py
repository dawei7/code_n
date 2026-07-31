"""Optimal app-local solution for LeetCode 1145."""

from __future__ import annotations

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


def solve(root: Any | None, n: int, x: int) -> bool:
    left_size = right_size = 0

    def count(node: Any | None) -> int:
        nonlocal left_size, right_size
        if node is None:
            return 0
        left = count(node.left)
        right = count(node.right)
        if node.val == x:
            left_size, right_size = left, right
        return left + right + 1

    count(root)
    parent_size = n - left_size - right_size - 1
    return max(left_size, right_size, parent_size) > n // 2
