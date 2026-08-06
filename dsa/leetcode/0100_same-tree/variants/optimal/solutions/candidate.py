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


def solve(p: TreeNode | None, q: TreeNode | None) -> bool:
    if p is None or q is None:
        return p is q
    return p.val == q.val and solve(p.left, q.left) and solve(p.right, q.right)
