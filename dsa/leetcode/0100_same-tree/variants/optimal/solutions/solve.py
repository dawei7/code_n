from typing import Optional


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


class Solution:
    def isSameTree(
        self,
        p: Optional["TreeNode"],  # noqa: F821
        q: Optional["TreeNode"],  # noqa: F821
    ) -> bool:
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def solve(p, q) -> bool:
    return Solution().isSameTree(p, q)
