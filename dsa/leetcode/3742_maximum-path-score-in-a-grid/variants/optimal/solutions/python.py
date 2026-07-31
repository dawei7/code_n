def solve(grid: list[list[int]], k: int) -> int:
    rows = len(grid)
    columns = len(grid[0])
    limit = min(k, rows + columns - 2)
    states: list[dict[int, int] | None] = [None] * columns

    for row in range(rows):
        for column in range(columns):
            value = grid[row][column]
            cell_cost = 0 if value == 0 else 1
            current: dict[int, int] = {}

            if row == 0 and column == 0:
                current[0] = 0
            else:
                predecessors = []
                if row > 0 and states[column] is not None:
                    predecessors.append(states[column])
                if column > 0 and states[column - 1] is not None:
                    predecessors.append(states[column - 1])

                for previous in predecessors:
                    for used, score in previous.items():
                        new_cost = used + cell_cost
                        if new_cost <= limit:
                            current[new_cost] = max(
                                current.get(new_cost, -1), score + value
                            )

            states[column] = current

    destination = states[-1]
    return max(destination.values()) if destination else -1
