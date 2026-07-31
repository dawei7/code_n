def solve(grid: list[list[str]]) -> bool:
    rows, columns = len(grid), len(grid[0])
    path_length = rows + columns - 1
    if path_length % 2 == 1 or grid[0][0] == ")" or grid[-1][-1] == "(":
        return False

    states = [set() for _ in range(columns)]
    for row in range(rows):
        for column in range(columns):
            previous: set[int] = set()
            if row == 0 and column == 0:
                previous.add(0)
            else:
                if row > 0:
                    previous.update(states[column])
                if column > 0:
                    previous.update(states[column - 1])

            delta = 1 if grid[row][column] == "(" else -1
            remaining = rows - row - 1 + columns - column - 1
            states[column] = {balance + delta for balance in previous if 0 <= balance + delta <= remaining}

    return 0 in states[-1]
