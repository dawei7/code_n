"""Iterative candidate for LeetCode 1430."""


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


def solve(root, arr: list[int]) -> bool:
    if root is None:
        return False

    last_position = len(arr) - 1
    stack = [(root, 0)]

    while stack:
        node, position = stack.pop()
        if node.val != arr[position]:
            continue

        is_leaf = node.left is None and node.right is None
        if position == last_position:
            if is_leaf:
                return True
            continue

        next_position = position + 1
        if node.right is not None:
            stack.append((node.right, next_position))
        if node.left is not None:
            stack.append((node.left, next_position))

    return False
