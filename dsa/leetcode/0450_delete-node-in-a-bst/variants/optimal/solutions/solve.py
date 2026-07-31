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


def solve(root: TreeNode | None, key: int) -> TreeNode | None:
    if root is None:
        return None
    if key < root.val:
        root.left = solve(root.left, key)
    elif key > root.val:
        root.right = solve(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        successor = root.right
        while successor.left is not None:
            successor = successor.left
        root.val = successor.val
        root.right = solve(root.right, successor.val)
    return root
