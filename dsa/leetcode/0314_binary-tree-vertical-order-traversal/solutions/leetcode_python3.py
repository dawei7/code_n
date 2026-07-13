from collections import defaultdict, deque
from typing import Any


def _vertical_order(root: Any | None) -> list[list[int]]:
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


class Solution:
    def verticalOrder(self, root: Any | None) -> list[list[int]]:
        return _vertical_order(root)
