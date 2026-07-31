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


def solve(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None or root is p or root is q:
        return root
    left = solve(root.left, p, q)
    right = solve(root.right, p, q)
    if left is not None and right is not None:
        return root
    return left if left is not None else right
