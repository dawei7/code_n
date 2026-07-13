from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        columns = len(board[0])
        for row in range(rows):
            for column in range(columns):
                neighbors = 0
                for row_offset in (-1, 0, 1):
                    for column_offset in (-1, 0, 1):
                        if row_offset == column_offset == 0:
                            continue
                        next_row = row + row_offset
                        next_column = column + column_offset
                        if (
                            0 <= next_row < rows
                            and 0 <= next_column < columns
                            and board[next_row][next_column] & 1
                        ):
                            neighbors += 1
                if neighbors == 3 or (neighbors == 2 and board[row][column] & 1):
                    board[row][column] |= 2
        for row in range(rows):
            for column in range(columns):
                board[row][column] >>= 1
