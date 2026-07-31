def solve(grid: list[list[int]], k: int) -> int:
    rows = len(grid)
    columns = len(grid[0])
    infinity = float("inf")
    cells = sorted((grid[row][column], row, column) for row in range(rows) for column in range(columns))
    cells.reverse()

    def close_normal_moves(costs: list[list[float]]) -> None:
        for row in range(rows):
            for column in range(columns):
                if row > 0:
                    costs[row][column] = min(
                        costs[row][column],
                        costs[row - 1][column] + grid[row][column],
                    )
                if column > 0:
                    costs[row][column] = min(
                        costs[row][column],
                        costs[row][column - 1] + grid[row][column],
                    )

    costs = [[infinity] * columns for _ in range(rows)]
    costs[0][0] = 0
    close_normal_moves(costs)

    for _ in range(k):
        next_costs = [row[:] for row in costs]
        best_source = infinity
        index = 0

        while index < len(cells):
            end = index
            value = cells[index][0]
            while end < len(cells) and cells[end][0] == value:
                _, row, column = cells[end]
                best_source = min(best_source, costs[row][column])
                end += 1
            for position in range(index, end):
                _, row, column = cells[position]
                next_costs[row][column] = min(next_costs[row][column], best_source)
            index = end

        close_normal_moves(next_costs)
        costs = next_costs

    return int(costs[-1][-1])
