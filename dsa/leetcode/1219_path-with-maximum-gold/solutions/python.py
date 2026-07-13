def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
            return 0
        gold = grid[r][c]
        grid[r][c] = 0
        best_next = 0
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            best_next = max(best_next, dfs(r + dr, c + dc))
        grid[r][c] = gold
        return gold + best_next

    answer = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                answer = max(answer, dfs(r, c))
    return answer
