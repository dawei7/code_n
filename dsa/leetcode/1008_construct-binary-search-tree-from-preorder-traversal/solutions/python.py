"""Optimal solution for LeetCode 1008: Construct Binary Search Tree from Preorder Traversal."""

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


def solve(preorder: list[int]) -> TreeNode | None:
    index = 0

    def build(upper: int) -> TreeNode | None:
        nonlocal index
        if index == len(preorder) or preorder[index] > upper:
            return None
        value = preorder[index]
        index += 1
        node = TreeNode(value)
        node.left = build(value)
        node.right = build(upper)
        return node

    return build(10**18)
