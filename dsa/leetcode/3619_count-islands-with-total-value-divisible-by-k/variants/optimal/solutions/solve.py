def solve(grid: list[list[int]], k: int) -> int:
    rows = len(grid)
    columns = len(grid[0])
    divisible_islands = 0

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] <= 0:
                continue

            total_modulo = 0
            stack = [(row, column)]
            grid[row][column] = -grid[row][column]

            while stack:
                current_row, current_column = stack.pop()
                total_modulo = (total_modulo - grid[current_row][current_column]) % k

                for next_row, next_column in (
                    (current_row - 1, current_column),
                    (current_row + 1, current_column),
                    (current_row, current_column - 1),
                    (current_row, current_column + 1),
                ):
                    if 0 <= next_row < rows and 0 <= next_column < columns and grid[next_row][next_column] > 0:
                        grid[next_row][next_column] = -grid[next_row][next_column]
                        stack.append((next_row, next_column))

            if total_modulo == 0:
                divisible_islands += 1

    return divisible_islands
