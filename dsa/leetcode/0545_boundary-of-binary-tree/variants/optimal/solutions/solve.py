"""Anti-clockwise binary-tree boundary for LeetCode 545."""


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


def solve(root) -> list[int]:
    if root is None:
        return []

    def is_leaf(node) -> bool:
        return node.left is None and node.right is None

    boundary = [root.val]

    node = root.left
    while node is not None:
        if not is_leaf(node):
            boundary.append(node.val)
        node = node.left if node.left is not None else node.right

    stack = [root]
    while stack:
        node = stack.pop()
        if is_leaf(node):
            if node is not root:
                boundary.append(node.val)
            continue
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    right_boundary = []
    node = root.right
    while node is not None:
        if not is_leaf(node):
            right_boundary.append(node.val)
        node = node.right if node.right is not None else node.left

    boundary.extend(reversed(right_boundary))
    return boundary
