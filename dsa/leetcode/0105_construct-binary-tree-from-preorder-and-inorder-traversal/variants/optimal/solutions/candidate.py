"""Candidate for LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal."""


class TreeNode:
    """Local equivalent of the binary-tree node supplied by LeetCode's judge."""

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
    position = {x: i for i, x in enumerate(inorder)}
    i = 0

    def build(left: int, right: int) -> TreeNode | None:
        nonlocal i
        if left > right:
            return None

        x = preorder[i]
        i += 1
        middle = position[x]
        node = TreeNode(x)
        node.left = build(left, middle - 1)
        node.right = build(middle + 1, right)
        return node

    return build(0, len(inorder) - 1)
