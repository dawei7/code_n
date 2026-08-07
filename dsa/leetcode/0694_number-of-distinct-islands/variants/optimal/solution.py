from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        shapes = set()

        for origin_row in range(rows):
            for origin_column in range(columns):
                origin = (origin_row, origin_column)
                if grid[origin_row][origin_column] == 0 or origin in visited:
                    continue

                visited.add(origin)
                stack = [origin]
                offsets = set()

                while stack:
                    row, column = stack.pop()
                    offsets.add((row - origin_row, column - origin_column))

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

                shapes.add(frozenset(offsets))

        return len(shapes)
