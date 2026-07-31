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
    current = root
    last_visited = None

    while current is not None or stack:
        if current is not None:
            stack.append(current)
            current = current.left
            continue

        node = stack[-1]
        if node.right is not None and last_visited is not node.right:
            current = node.right
        else:
            result.append(node.val)
            last_visited = stack.pop()
    return result
