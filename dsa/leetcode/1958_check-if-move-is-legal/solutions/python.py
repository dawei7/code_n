def solve(
    board: list[list[str]],
    rMove: int,
    cMove: int,
    color: str,
) -> bool:
    opposite = "W" if color == "B" else "B"

    for row_step in (-1, 0, 1):
        for column_step in (-1, 0, 1):
            if row_step == column_step == 0:
                continue

            row = rMove + row_step
            column = cMove + column_step
            has_middle = False

            while (
                0 <= row < 8
                and 0 <= column < 8
                and board[row][column] == opposite
            ):
                has_middle = True
                row += row_step
                column += column_step

            if (
                has_middle
                and 0 <= row < 8
                and 0 <= column < 8
                and board[row][column] == color
            ):
                return True

    return False
