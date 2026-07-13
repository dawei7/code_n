from collections import deque
from typing import Any


def solve(root: Any | None) -> list[list[int]]:
    if root is None:
        return []
    levels: deque[list[int]] = deque()
    queue = deque([root])
    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        levels.appendleft(level)
    return list(levels)
