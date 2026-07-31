from typing import Any


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


def solve(root: Any | None) -> list[int]:
    result: list[int] = []
    stack: list[Any] = []
    node = root

    while node is not None or stack:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right

    return result
