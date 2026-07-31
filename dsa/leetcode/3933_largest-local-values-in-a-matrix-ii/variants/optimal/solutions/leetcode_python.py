class Solution:
    def countLocalMaximums(self, matrix: list[list[int]]) -> int:
        rows, columns = len(matrix), len(matrix[0])
        positions = [[] for _ in range(201)]

        for row in range(rows):
            for column in range(columns):
                value = matrix[row][column]
                if value:
                    positions[value].append((row, column))

        greater = [[0] * columns for _ in range(rows)]
        answer = 0

        for value in range(200, 0, -1):
            cells = positions[value]
            if cells:
                prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
                for row in range(rows):
                    running = 0
                    above = prefix[row]
                    current = prefix[row + 1]
                    flags = greater[row]
                    for column in range(columns):
                        running += flags[column]
                        current[column + 1] = above[column + 1] + running

                for row, column in cells:
                    top = max(0, row - value)
                    bottom = min(rows - 1, row + value)
                    left = max(0, column - value)
                    right = min(columns - 1, column + value)
                    larger = (
                        prefix[bottom + 1][right + 1]
                        - prefix[top][right + 1]
                        - prefix[bottom + 1][left]
                        + prefix[top][left]
                    )

                    for corner_row in (row - value, row + value):
                        if 0 <= corner_row < rows:
                            for corner_column in (
                                column - value,
                                column + value,
                            ):
                                if 0 <= corner_column < columns and matrix[corner_row][corner_column] > value:
                                    larger -= 1

                    if larger == 0:
                        answer += 1

            for row, column in cells:
                greater[row][column] = 1

        return answer
