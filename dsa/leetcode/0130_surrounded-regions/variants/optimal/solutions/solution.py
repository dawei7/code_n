from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows = len(board)
        columns = len(board[0])
        queue = deque()

        def preserve(row, column):
            if 0 <= row < rows and 0 <= column < columns and board[row][column] == "O":
                board[row][column] = "#"
                queue.append((row, column))

        for row in range(rows):
            preserve(row, 0)
            preserve(row, columns - 1)
        for column in range(columns):
            preserve(0, column)
            preserve(rows - 1, column)

        while queue:
            row, column = queue.popleft()
            preserve(row + 1, column)
            preserve(row - 1, column)
            preserve(row, column + 1)
            preserve(row, column - 1)

        for row in range(rows):
            for column in range(columns):
                board[row][column] = "O" if board[row][column] == "#" else "X"
