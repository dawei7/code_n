"""Optimal app-local solution for LeetCode 847."""

from collections import deque


def solve(graph):
    node_count = len(graph)
    if node_count == 1:
        return 0

    full_mask = (1 << node_count) - 1
    queue = deque((node, 1 << node, 0) for node in range(node_count))
    seen = {(node, 1 << node) for node in range(node_count)}

    while queue:
        node, mask, distance = queue.popleft()
        for neighbor in graph[node]:
            next_mask = mask | (1 << neighbor)
            if next_mask == full_mask:
                return distance + 1
            state = (neighbor, next_mask)
            if state not in seen:
                seen.add(state)
                queue.append((neighbor, next_mask, distance + 1))

    return 0
