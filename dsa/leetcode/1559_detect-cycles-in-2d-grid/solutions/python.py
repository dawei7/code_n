def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    seen = [[False] * cols for _ in range(rows)]

    def dfs(r, c, pr, pc, value):
        seen[r][c] = True
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            if grid[nr][nc] != value:
                continue
            if nr == pr and nc == pc:
                continue
            if seen[nr][nc] or dfs(nr, nc, r, c, value):
                return True
        return False

    for r in range(rows):
        for c in range(cols):
            if not seen[r][c] and dfs(r, c, -1, -1, grid[r][c]):
                return True
    return False
