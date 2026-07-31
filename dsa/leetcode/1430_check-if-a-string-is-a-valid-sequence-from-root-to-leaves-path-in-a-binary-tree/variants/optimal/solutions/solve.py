"""Optimal app-local solution for LeetCode 1430."""


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


def solve(root, arr: list[int]) -> bool:
    def matches(node, index: int) -> bool:
        if node is None or index == len(arr) or node.val != arr[index]:
            return False
        if node.left is None and node.right is None:
            return index == len(arr) - 1
        return matches(node.left, index + 1) or matches(node.right, index + 1)

    return matches(root, 0)
