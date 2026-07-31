def solve(grid: list[list[int]]) -> int:
    mod = 1_000_000_007
    rows = len(grid)
    columns = len(grid[0])
    from_above = [0] * columns

    for row in range(rows):
        from_left = 0
        for column in range(columns):
            if row == 0 and column == 0:
                total = 1
                from_left = total
                from_above[column] = total
            elif grid[row][column] == 0:
                total = (from_left + from_above[column]) % mod
                from_left = total
                from_above[column] = total
            else:
                from_left, from_above[column] = (
                    from_above[column],
                    from_left,
                )

    return from_left
