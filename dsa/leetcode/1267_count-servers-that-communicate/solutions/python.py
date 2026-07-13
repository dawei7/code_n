def solve(grid):
    row_counts = [sum(row) for row in grid]
    col_counts = [sum(grid[r][c] for r in range(len(grid))) for c in range(len(grid[0]))]
    answer = 0
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value and (row_counts[r] > 1 or col_counts[c] > 1):
                answer += 1
    return answer
