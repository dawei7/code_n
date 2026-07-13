def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    def is_land(value):
        return value == 1

    def island_count(skip=None):
        seen = [[False] * cols for _ in range(rows)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                if skip == (r, c) or seen[r][c] or not is_land(grid[r][c]):
                    continue
                count += 1
                stack = [(r, c)]
                seen[r][c] = True
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr = cr + dr
                        nc = cc + dc
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            continue
                        if skip == (nr, nc) or seen[nr][nc] or not is_land(grid[nr][nc]):
                            continue
                        seen[nr][nc] = True
                        stack.append((nr, nc))
        return count

    if island_count() != 1:
        return 0
    for r in range(rows):
        for c in range(cols):
            if is_land(grid[r][c]) and island_count((r, c)) != 1:
                return 1
    return 2
