from typing import List


class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        shapes = set()

        def canonical(points):
            transformed = [[] for _ in range(8)]
            for x, y in points:
                variants = (
                    (x, y),
                    (x, -y),
                    (-x, y),
                    (-x, -y),
                    (y, x),
                    (y, -x),
                    (-y, x),
                    (-y, -x),
                )
                for index, point in enumerate(variants):
                    transformed[index].append(point)

            normalized = []
            for orientation in transformed:
                minimum_x = min(x for x, _ in orientation)
                minimum_y = min(y for _, y in orientation)
                normalized.append(frozenset(
                    (x - minimum_x, y - minimum_y)
                    for x, y in orientation
                ))
            return frozenset(normalized)

        for start_row in range(rows):
            for start_column in range(columns):
                start = (start_row, start_column)
                if grid[start_row][start_column] == 0 or start in visited:
                    continue

                visited.add(start)
                stack = [start]
                points = []

                while stack:
                    row, column = stack.pop()
                    points.append((row - start_row, column - start_column))
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

                shapes.add(canonical(points))

        return len(shapes)
