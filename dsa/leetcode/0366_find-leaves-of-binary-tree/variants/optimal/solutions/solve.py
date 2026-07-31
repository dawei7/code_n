"""Optimal solution for LeetCode 366: Find Leaves of Binary Tree."""


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


def solve(root) -> list[list[int]]:
    rounds: list[list[int]] = []

    def leaf_height(node) -> int:
        if node is None:
            return -1
        height = 1 + max(leaf_height(node.left), leaf_height(node.right))
        if height == len(rounds):
            rounds.append([])
        rounds[height].append(node.val)
        return height

    leaf_height(root)
    return rounds
