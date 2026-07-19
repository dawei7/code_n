def solve(
    startPos: list[int],
    homePos: list[int],
    rowCosts: list[int],
    colCosts: list[int],
) -> int:
    total = 0

    row_step = 1 if startPos[0] < homePos[0] else -1
    for row in range(startPos[0] + row_step, homePos[0] + row_step, row_step):
        total += rowCosts[row]

    col_step = 1 if startPos[1] < homePos[1] else -1
    for column in range(
        startPos[1] + col_step,
        homePos[1] + col_step,
        col_step,
    ):
        total += colCosts[column]

    return total
