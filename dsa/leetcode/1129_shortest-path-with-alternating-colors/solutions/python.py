"""Optimal app-local solution for LeetCode 1129."""

from collections import deque


def solve(n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
    adjacency = [[[] for _ in range(n)] for _ in range(2)]
    for source, target in redEdges:
        adjacency[0][source].append(target)
    for source, target in blueEdges:
        adjacency[1][source].append(target)

    distances = [[-1, -1] for _ in range(n)]
    distances[0] = [0, 0]
    queue = deque([(0, 0), (0, 1)])

    while queue:
        node, last_color = queue.popleft()
        next_color = 1 - last_color
        for neighbor in adjacency[next_color][node]:
            if distances[neighbor][next_color] != -1:
                continue
            distances[neighbor][next_color] = distances[node][last_color] + 1
            queue.append((neighbor, next_color))

    return [
        max(red_distance, blue_distance)
        if min(red_distance, blue_distance) == -1
        else min(red_distance, blue_distance)
        for red_distance, blue_distance in distances
    ]
