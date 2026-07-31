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


def solve(root, val):
    inserted = TreeNode(val)

    if val > root.val:
        inserted.left = root
        return inserted

    current = root
    while current.right is not None and current.right.val > val:
        current = current.right

    inserted.left = current.right
    current.right = inserted
    return root
