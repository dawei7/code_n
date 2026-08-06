"""Candidate for LeetCode 106: Construct Binary Tree from Inorder and Postorder Traversal."""


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


def solve(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    position = {x: i for i, x in enumerate(inorder)}
    i = len(postorder) - 1

    def build(left: int, right: int) -> TreeNode | None:
        nonlocal i
        if left > right:
            return None

        x = postorder[i]
        i -= 1
        middle = position[x]
        node = TreeNode(x)
        node.right = build(middle + 1, right)
        node.left = build(left, middle - 1)
        return node

    return build(0, len(inorder) - 1)
