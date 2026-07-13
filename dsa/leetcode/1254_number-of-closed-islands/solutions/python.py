def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    def flood(r, c):
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        if grid[r][c] == 1:
            return True
        grid[r][c] = 1
        closed = True
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            closed = flood(r + dr, c + dc) and closed
        return closed

    answer = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and flood(r, c):
                answer += 1
    return answer
