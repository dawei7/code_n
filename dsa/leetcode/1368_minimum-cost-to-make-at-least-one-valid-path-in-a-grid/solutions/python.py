"""Optimal solution for LeetCode 1368: Minimum Cost to Make at Least One Valid Path in a Grid."""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(grid), len(grid[0])
    dist = [[10**9] * cols for _ in range(rows)]
    dist[0][0] = 0
    queue: deque[tuple[int, int]] = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()
        for index, (dr, dc) in enumerate(directions, start=1):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cost = 0 if grid[r][c] == index else 1
                new_dist = dist[r][c] + cost
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    if cost == 0:
                        queue.appendleft((nr, nc))
                    else:
                        queue.append((nr, nc))
    return dist[-1][-1]
