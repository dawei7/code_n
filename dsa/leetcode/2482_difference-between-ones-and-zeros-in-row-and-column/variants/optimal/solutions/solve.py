def solve(grid):
    row_count = len(grid)
    column_count = len(grid[0])
    row_balance = [2 * sum(row) - column_count for row in grid]
    column_ones = [0] * column_count

    for row in grid:
        for column, value in enumerate(row):
            column_ones[column] += value

    column_balance = [2 * ones - row_count for ones in column_ones]
    return [[row_balance[row] + column_balance[column] for column in range(column_count)] for row in range(row_count)]
