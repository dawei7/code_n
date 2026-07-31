"""Optimal solution for LeetCode 106: Construct Binary Tree from Inorder and Postorder Traversal."""


class TreeNode:
    """Local equivalent of the binary-tree node supplied by LeetCode's judge."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(inorder: list[int], postorder: list[int]):
    index_by_value = {value: index for index, value in enumerate(inorder)}
    postorder_index = len(postorder) - 1

    def build(left: int, right: int):
        nonlocal postorder_index
        if left > right:
            return None
        value = postorder[postorder_index]
        postorder_index -= 1
        middle = index_by_value[value]
        node = TreeNode(value)
        node.right = build(middle + 1, right)
        node.left = build(left, middle - 1)
        return node

    return build(0, len(inorder) - 1)
