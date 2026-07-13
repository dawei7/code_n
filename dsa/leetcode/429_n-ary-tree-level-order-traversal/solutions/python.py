"""Optimal app-local solution for LeetCode 429."""

from collections import deque


def solve(root):
    if root is None:
        return []

    answer: list[list[int]] = []
    queue = deque([root])
    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            value, children = queue.popleft()
            level.append(value)
            queue.extend(children)
        answer.append(level)
    return answer
