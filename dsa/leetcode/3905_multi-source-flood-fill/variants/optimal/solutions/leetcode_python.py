class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0] * m for _ in range(n)]
        frontier = []

        for row, column, color in sources:
            grid[row][column] = color
            frontier.append((row, column))

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while frontier:
            next_colors = {}

            for row, column in frontier:
                color = grid[row][column]
                for row_delta, column_delta in directions:
                    next_row = row + row_delta
                    next_column = column + column_delta

                    if not (0 <= next_row < n and 0 <= next_column < m and grid[next_row][next_column] == 0):
                        continue

                    cell = (next_row, next_column)
                    next_colors[cell] = max(next_colors.get(cell, 0), color)

            frontier = []
            for (row, column), color in next_colors.items():
                grid[row][column] = color
                frontier.append((row, column))

        return grid
