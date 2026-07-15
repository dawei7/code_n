"""Optimal app-local solution for LeetCode 889."""

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


def solve(preorder, postorder):
    postorder_index = {value: index for index, value in enumerate(postorder)}
    preorder_index = 0

    def build(left, right):
        nonlocal preorder_index
        root = TreeNode(preorder[preorder_index])
        preorder_index += 1
        if left == right:
            return root

        first_child_root = preorder[preorder_index]
        first_child_end = postorder_index[first_child_root]
        root.left = build(left, first_child_end)
        if first_child_end + 1 < right:
            root.right = build(first_child_end + 1, right - 1)
        return root

    return build(0, len(postorder) - 1)
