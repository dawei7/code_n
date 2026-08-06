"""Breadth-first vertical buckets for LeetCode 314."""

from collections import defaultdict, deque


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


def _vertical_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    columns: dict[int, list[int]] = defaultdict(list)
    leftmost = 0
    rightmost = 0
    queue = deque([(root, 0)])
    while queue:
        node, column = queue.popleft()
        columns[column].append(node.val)
        leftmost = min(leftmost, column)
        rightmost = max(rightmost, column)
        if node.left is not None:
            queue.append((node.left, column - 1))
        if node.right is not None:
            queue.append((node.right, column + 1))
    return [columns[column] for column in range(leftmost, rightmost + 1)]


def solve(root: TreeNode | None) -> list[list[int]]:
    return _vertical_order(root)
