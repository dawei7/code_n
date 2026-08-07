from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = [[False] * columns for _ in range(rows)]
        maximum = 0

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0 or visited[row][column]:
                    continue

                visited[row][column] = True
                stack = [(row, column)]
                component = 0

                while stack:
                    current_row, current_column = stack.pop()
                    component += grid[current_row][current_column]

                    for row_delta, column_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = current_row + row_delta
                        next_column = current_column + column_delta
                        if (
                            0 <= next_row < rows
                            and 0 <= next_column < columns
                            and grid[next_row][next_column] > 0
                            and not visited[next_row][next_column]
                        ):
                            visited[next_row][next_column] = True
                            stack.append((next_row, next_column))

                maximum = max(maximum, component)

        return maximum
