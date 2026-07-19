def solve(room: list[list[int]]) -> int:
    rows = len(room)
    columns = len(room[0])
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    row = column = direction = 0
    states = set()
    cleaned = set()

    while (row, column, direction) not in states:
        states.add((row, column, direction))
        cleaned.add((row, column))

        row_step, column_step = directions[direction]
        next_row = row + row_step
        next_column = column + column_step
        if (
            next_row < 0
            or next_row >= rows
            or next_column < 0
            or next_column >= columns
            or room[next_row][next_column] == 1
        ):
            direction = (direction + 1) % 4
        else:
            row = next_row
            column = next_column

    return len(cleaned)
