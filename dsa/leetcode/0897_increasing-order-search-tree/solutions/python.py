"""Optimal app-local solution for LeetCode 897."""

from __future__ import annotations


class TreeNode:
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
    dummy = TreeNode()
    tail = dummy
    stack = []
    current = root

    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        original_right = current.right
        current.left = None
        tail.right = current
        tail = current
        current = original_right

    tail.right = None
    return dummy.right
