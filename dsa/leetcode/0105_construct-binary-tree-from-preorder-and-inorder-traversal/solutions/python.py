"""Optimal solution for LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal."""

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


def solve(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    index_by_value = {value: i for i, value in enumerate(inorder)}
    preorder_index = 0

    def build(left: int, right: int) -> TreeNode | None:
        nonlocal preorder_index
        if left > right:
            return None
        value = preorder[preorder_index]
        preorder_index += 1
        mid = index_by_value[value]
        node = TreeNode(value)
        node.left = build(left, mid - 1)
        node.right = build(mid + 1, right)
        return node

    return build(0, len(inorder) - 1)
