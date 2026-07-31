from collections import deque
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


def solve(root: Any | None) -> list[list[int]]:
    if root is None:
        return []

    result: list[list[int]] = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level: deque[int] = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(list(level))
        left_to_right = not left_to_right
    return result
