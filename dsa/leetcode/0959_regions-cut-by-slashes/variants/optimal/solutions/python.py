"""Optimal app-local solution for LeetCode 959."""


def solve(grid):
    side = 3 * len(grid)
    blocked = [[False] * side for _ in range(side)]

    for row, text in enumerate(grid):
        for column, character in enumerate(text):
            if character == "/":
                for offset in range(3):
                    blocked[3 * row + offset][3 * column + 2 - offset] = True
            elif character == "\\":
                for offset in range(3):
                    blocked[3 * row + offset][3 * column + offset] = True

    regions = 0
    for row in range(side):
        for column in range(side):
            if blocked[row][column]:
                continue
            regions += 1
            blocked[row][column] = True
            stack = [(row, column)]
            while stack:
                current_row, current_column = stack.pop()
                for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + row_step
                    next_column = current_column + column_step
                    if (
                        0 <= next_row < side
                        and 0 <= next_column < side
                        and not blocked[next_row][next_column]
                    ):
                        blocked[next_row][next_column] = True
                        stack.append((next_row, next_column))
    return regions
