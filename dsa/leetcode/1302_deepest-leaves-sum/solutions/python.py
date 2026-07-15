"""Optimal app-local solution for LeetCode 1302."""

from collections import deque


def solve(root):
    queue = deque([root])
    level_sum = 0

    while queue:
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return level_sum
