"""Optimal solution for LeetCode 106: Construct Binary Tree from Inorder and Postorder Traversal."""

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


def solve(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    index_by_value = {value: i for i, value in enumerate(inorder)}
    postorder_index = len(postorder) - 1

    def build(left: int, right: int) -> TreeNode | None:
        nonlocal postorder_index
        if left > right:
            return None
        value = postorder[postorder_index]
        postorder_index -= 1
        mid = index_by_value[value]
        node = TreeNode(value)
        node.right = build(mid + 1, right)
        node.left = build(left, mid - 1)
        return node

    return build(0, len(inorder) - 1)
