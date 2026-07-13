def solve(grid, k):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    total = rows * cols
    k %= total
    flat = [grid[r][c] for r in range(rows) for c in range(cols)]
    shifted = flat[-k:] + flat[:-k] if k else flat
    return [shifted[i * cols:(i + 1) * cols] for i in range(rows)]
