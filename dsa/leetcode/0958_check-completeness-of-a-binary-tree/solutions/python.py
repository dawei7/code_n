"""Optimal app-local solution for LeetCode 958."""

from collections import deque


def solve(root):
    queue = deque([root])
    missing_seen = False

    while queue:
        node = queue.popleft()
        if node is None:
            missing_seen = True
            continue
        if missing_seen:
            return False
        queue.append(node.left)
        queue.append(node.right)
    return True
