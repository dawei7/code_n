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


def solve(root, level: int) -> int:
    current = [root]
    depth = 0

    while current:
        if depth == level:
            return current[len(current) // 2].val

        following = []
        for node in current:
            if node.left is not None:
                following.append(node.left)
            if node.right is not None:
                following.append(node.right)

        current = following
        depth += 1

    return -1
