from typing import List


class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        board = [[-1] * n for _ in range(m)]
        moves = (
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1),
        )

        def available_degree(row: int, column: int) -> int:
            degree = 0
            for row_change, column_change in moves:
                next_row = row + row_change
                next_column = column + column_change
                if (
                    0 <= next_row < m
                    and 0 <= next_column < n
                    and board[next_row][next_column] == -1
                ):
                    degree += 1
            return degree

        def search(row: int, column: int, visit: int) -> bool:
            if visit == m * n:
                return True

            candidates = []
            for row_change, column_change in moves:
                next_row = row + row_change
                next_column = column + column_change
                if (
                    0 <= next_row < m
                    and 0 <= next_column < n
                    and board[next_row][next_column] == -1
                ):
                    candidates.append((available_degree(next_row, next_column), next_row, next_column))

            candidates.sort()
            for _, next_row, next_column in candidates:
                board[next_row][next_column] = visit
                if search(next_row, next_column, visit + 1):
                    return True
                board[next_row][next_column] = -1
            return False

        board[r][c] = 0
        search(r, c, 1)
        return board
