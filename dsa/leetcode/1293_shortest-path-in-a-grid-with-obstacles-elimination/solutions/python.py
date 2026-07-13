from collections import deque


def solve(grid, k):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    if rows == 1 and cols == 1:
        return 0
    if k >= rows + cols - 3:
        return rows + cols - 2

    queue = deque([(0, 0, k, 0)])
    best_remaining = {(0, 0): k}
    while queue:
        r, c, remaining, steps = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            next_remaining = remaining - grid[nr][nc]
            if next_remaining < 0:
                continue
            if nr == rows - 1 and nc == cols - 1:
                return steps + 1
            if best_remaining.get((nr, nc), -1) >= next_remaining:
                continue
            best_remaining[(nr, nc)] = next_remaining
            queue.append((nr, nc, next_remaining, steps + 1))
    return -1
