def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    def dfs(row: int, column: int) -> int:
        if not (0 <= row < rows and 0 <= column < cols) or grid[row][column] == 0:
            return 0
        gold = grid[row][column]
        grid[row][column] = 0
        best_next = 0
        for row_change, column_change in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            best_next = max(best_next, dfs(row + row_change, column + column_change))
        grid[row][column] = gold
        return gold + best_next

    answer = 0
    for row in range(rows):
        for column in range(cols):
            if grid[row][column]:
                answer = max(answer, dfs(row, column))
    return answer
