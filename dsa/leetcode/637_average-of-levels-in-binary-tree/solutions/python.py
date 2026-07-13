from collections import deque
from typing import Any


def solve(root: Any) -> list[float]:
    averages: list[float] = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        averages.append(level_sum / level_size)

    return averages
