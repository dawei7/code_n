def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    previous = [set() for _ in range(columns)]

    for row in range(rows):
        current = []

        for column in range(columns):
            value = grid[row][column]

            if row == 0 and column == 0:
                states = {value}
            else:
                states = set()

                if row > 0:
                    for path_xor in previous[column]:
                        states.add(path_xor ^ value)

                if column > 0:
                    for path_xor in current[column - 1]:
                        states.add(path_xor ^ value)

            current.append(states)

        previous = current

    return min(previous[-1])
