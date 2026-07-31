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


def solve(root) -> list[str]:
    paths: list[str] = []

    def visit(node, prefix: str) -> None:
        if node is None:
            return
        path = f"{prefix}->{node.val}" if prefix else str(node.val)
        if node.left is None and node.right is None:
            paths.append(path)
            return
        visit(node.left, path)
        visit(node.right, path)

    visit(root, "")
    return paths
