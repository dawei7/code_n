class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode | None) -> TreeNode | None:
    if root is None:
        return None
    root.left = solve(root.left)
    root.right = solve(root.right)
    if root.val == 0 and root.left is None and root.right is None:
        return None
    return root
