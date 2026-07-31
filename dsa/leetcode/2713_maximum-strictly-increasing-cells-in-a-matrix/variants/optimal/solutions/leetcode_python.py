class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        columns = len(mat[0])
        positions = {}

        for row in range(rows):
            for column in range(columns):
                positions.setdefault(mat[row][column], []).append((row, column))

        row_best = [0] * rows
        column_best = [0] * columns
        answer = 0

        for value in sorted(positions):
            updates = []
            for row, column in positions[value]:
                length = 1 + max(row_best[row], column_best[column])
                updates.append((row, column, length))
                answer = max(answer, length)

            for row, column, length in updates:
                row_best[row] = max(row_best[row], length)
                column_best[column] = max(column_best[column], length)

        return answer

