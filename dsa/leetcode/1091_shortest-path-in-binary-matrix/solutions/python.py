"""Optimal solution for LeetCode 1091: Shortest Path in Binary Matrix."""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    n = len(grid)
    if grid[0][0] or grid[-1][-1]:
        return -1
    queue: deque[tuple[int, int, int]] = deque([(0, 0, 1)])
    grid[0][0] = 1
    while queue:
        r, c, dist = queue.popleft()
        if r == n - 1 and c == n - 1:
            return dist
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))
    return -1
