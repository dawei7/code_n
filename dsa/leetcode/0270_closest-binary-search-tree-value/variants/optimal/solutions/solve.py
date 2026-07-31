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


def solve(root, target: float) -> int:
    closest = root.val
    node = root
    while node is not None:
        if (abs(node.val - target), node.val) < (abs(closest - target), closest):
            closest = node.val
        if node.val == target:
            return node.val
        node = node.left if target < node.val else node.right
    return closest
