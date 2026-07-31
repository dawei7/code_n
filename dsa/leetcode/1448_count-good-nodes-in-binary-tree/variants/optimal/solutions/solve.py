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


def solve(root):
    good = 0
    stack = [(root, root.val)]

    while stack:
        node, path_maximum = stack.pop()
        if node.val >= path_maximum:
            good += 1

        next_maximum = max(path_maximum, node.val)
        if node.left is not None:
            stack.append((node.left, next_maximum))
        if node.right is not None:
            stack.append((node.right, next_maximum))

    return good
