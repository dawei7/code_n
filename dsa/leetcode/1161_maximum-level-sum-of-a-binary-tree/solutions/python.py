"""Optimal app-local solution for LeetCode 1161."""

from collections import deque
from typing import Any


def solve(root: Any) -> int:
    queue = deque([root])
    level = 1
    best_level = 1
    best_sum = float("-inf")

    while queue:
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        if level_sum > best_sum:
            best_sum = level_sum
            best_level = level
        level += 1

    return best_level
