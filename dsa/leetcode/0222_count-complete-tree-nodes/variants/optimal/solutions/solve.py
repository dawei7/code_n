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


def solve(root: TreeNode | None) -> int:
    def left_height(node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    if not root:
        return 0
    left = left_height(root.left)
    right = left_height(root.right)
    if left == right:
        return (1 << left) + solve(root.right)
    return (1 << right) + solve(root.left)
