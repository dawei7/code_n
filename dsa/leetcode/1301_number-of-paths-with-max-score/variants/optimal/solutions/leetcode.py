from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        modulus = 1_000_000_007
        n = len(board)
        scores = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]
        scores[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        for row in range(n - 1, -1, -1):
            for column in range(n - 1, -1, -1):
                if board[row][column] == "X" or (row == n - 1 and column == n - 1):
                    continue

                best_score = -1
                best_ways = 0
                for next_row, next_column in (
                    (row + 1, column),
                    (row, column + 1),
                    (row + 1, column + 1),
                ):
                    if next_row >= n or next_column >= n or scores[next_row][next_column] < 0:
                        continue
                    if scores[next_row][next_column] > best_score:
                        best_score = scores[next_row][next_column]
                        best_ways = ways[next_row][next_column]
                    elif scores[next_row][next_column] == best_score:
                        best_ways = (best_ways + ways[next_row][next_column]) % modulus

                if best_score >= 0:
                    cell_value = 0 if board[row][column] == "E" else int(board[row][column])
                    scores[row][column] = best_score + cell_value
                    ways[row][column] = best_ways

        if scores[0][0] < 0:
            return [0, 0]
        return [scores[0][0], ways[0][0] % modulus]
