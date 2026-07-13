"""Optimal solution for LeetCode 1020: Number of Enclaves."""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue: deque[tuple[int, int]] = deque()

    for r in range(rows):
        for c in (0, cols - 1):
            if grid[r][c] == 1:
                grid[r][c] = 0
                queue.append((r, c))
    for c in range(cols):
        for r in (0, rows - 1):
            if grid[r][c] == 1:
                grid[r][c] = 0
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 0
                queue.append((nr, nc))

    return sum(sum(row) for row in grid)
