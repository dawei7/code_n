"""Reference solution for LeetCode 1379."""


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


def solve(original, cloned, target):
    stack = [(original, cloned)]

    while stack:
        original_node, cloned_node = stack.pop()
        if original_node is target:
            return cloned_node

        if original_node.right is not None:
            stack.append((original_node.right, cloned_node.right))
        if original_node.left is not None:
            stack.append((original_node.left, cloned_node.left))
