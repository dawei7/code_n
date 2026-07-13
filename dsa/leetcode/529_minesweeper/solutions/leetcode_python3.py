from collections import deque
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        start_row, start_col = click
        if board[start_row][start_col] == "M":
            board[start_row][start_col] = "X"
            return board

        rows, cols = len(board), len(board[0])
        queue = deque([(start_row, start_col)])
        board[start_row][start_col] = "B"

        while queue:
            row, col = queue.popleft()
            neighbors = [
                (next_row, next_col)
                for next_row in range(max(0, row - 1), min(rows, row + 2))
                for next_col in range(max(0, col - 1), min(cols, col + 2))
                if (next_row, next_col) != (row, col)
            ]
            mines = sum(board[next_row][next_col] == "M" for next_row, next_col in neighbors)
            if mines:
                board[row][col] = str(mines)
                continue

            for next_row, next_col in neighbors:
                if board[next_row][next_col] == "E":
                    board[next_row][next_col] = "B"
                    queue.append((next_row, next_col))

        return board
