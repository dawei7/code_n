def solve(grid: list[list[int]]) -> int:
    size = len(grid)
    unreachable = -10**9
    previous = [[unreachable] * size for _ in range(size)]
    previous[0][0] = grid[0][0]

    for step in range(1, 2 * size - 1):
        current = [[unreachable] * size for _ in range(size)]
        row_start = max(0, step - size + 1)
        row_end = min(size - 1, step)

        for first_row in range(row_start, row_end + 1):
            first_column = step - first_row
            if grid[first_row][first_column] == -1:
                continue
            for second_row in range(row_start, row_end + 1):
                second_column = step - second_row
                if grid[second_row][second_column] == -1:
                    continue

                best = previous[first_row][second_row]
                if first_row > 0:
                    best = max(best, previous[first_row - 1][second_row])
                if second_row > 0:
                    best = max(best, previous[first_row][second_row - 1])
                if first_row > 0 and second_row > 0:
                    best = max(best, previous[first_row - 1][second_row - 1])
                if best == unreachable:
                    continue

                cherries = grid[first_row][first_column]
                if first_row != second_row:
                    cherries += grid[second_row][second_column]
                current[first_row][second_row] = best + cherries

        previous = current

    return max(0, previous[size - 1][size - 1])
