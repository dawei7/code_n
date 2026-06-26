"""Optimal solution for LeetCode 1391: Check if There is a Valid Path in a Grid."""

from collections import deque


def solve(grid: list[list[int]]) -> bool:
    openings = {
        1: [(0, -1), (0, 1)],
        2: [(-1, 0), (1, 0)],
        3: [(0, -1), (1, 0)],
        4: [(0, 1), (1, 0)],
        5: [(0, -1), (-1, 0)],
        6: [(0, 1), (-1, 0)],
    }
    rows, cols = len(grid), len(grid[0])
    queue: deque[tuple[int, int]] = deque([(0, 0)])
    seen = {(0, 0)}

    while queue:
        r, c = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return True
        for dr, dc in openings[grid[r][c]]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in seen:
                continue
            if (-dr, -dc) in openings[grid[nr][nc]]:
                seen.add((nr, nc))
                queue.append((nr, nc))
    return False
