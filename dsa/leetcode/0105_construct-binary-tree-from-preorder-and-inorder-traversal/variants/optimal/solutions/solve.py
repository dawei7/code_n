"""Optimal solution for LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal."""


class TreeNode:
    """Local equivalent of the binary-tree node supplied by LeetCode's judge."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(preorder: list[int], inorder: list[int]):
    index_by_value = {value: index for index, value in enumerate(inorder)}
    preorder_index = 0

    def build(left: int, right: int):
        nonlocal preorder_index
        if left > right:
            return None
        value = preorder[preorder_index]
        preorder_index += 1
        middle = index_by_value[value]
        node = TreeNode(value)
        node.left = build(left, middle - 1)
        node.right = build(middle + 1, right)
        return node

    return build(0, len(inorder) - 1)
