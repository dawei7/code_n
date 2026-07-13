from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        maximum_area = 0

        for start_row in range(rows):
            for start_column in range(columns):
                start = (start_row, start_column)
                if grid[start_row][start_column] == 0 or start in visited:
                    continue

                visited.add(start)
                stack = [start]
                area = 0

                while stack:
                    row, column = stack.pop()
                    area += 1

                    for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = row + row_step
                        next_column = column + column_step
                        neighbor = (next_row, next_column)
                        if (
                            0 <= next_row < rows
                            and 0 <= next_column < columns
                            and grid[next_row][next_column] == 1
                            and neighbor not in visited
                        ):
                            visited.add(neighbor)
                            stack.append(neighbor)

                maximum_area = max(maximum_area, area)

        return maximum_area
