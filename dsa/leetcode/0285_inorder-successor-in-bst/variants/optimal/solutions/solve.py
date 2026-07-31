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


def solve(root: TreeNode, p: TreeNode) -> TreeNode | None:
    successor = None
    node = root
    while node is not None:
        if node.val > p.val:
            successor = node
            node = node.left
        else:
            node = node.right
    return successor
