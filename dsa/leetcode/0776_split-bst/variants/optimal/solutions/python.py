class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode | None, target: int) -> list[TreeNode | None]:
    if root is None:
        return [None, None]
    if root.val <= target:
        smaller_right, greater = solve(root.right, target)
        root.right = smaller_right
        return [root, greater]

    smaller, greater_left = solve(root.left, target)
    root.left = greater_left
    return [smaller, root]
