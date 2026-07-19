"""Optimal app-local solution for LeetCode 999."""


def solve(board):
    rook_row = rook_column = -1
    for row in range(8):
        for column in range(8):
            if board[row][column] == "R":
                rook_row, rook_column = row, column
                break
        if rook_row != -1:
            break

    captures = 0
    for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        row = rook_row + row_step
        column = rook_column + column_step
        while 0 <= row < 8 and 0 <= column < 8:
            piece = board[row][column]
            if piece == "B":
                break
            if piece == "p":
                captures += 1
                break
            row += row_step
            column += column_step

    return captures
