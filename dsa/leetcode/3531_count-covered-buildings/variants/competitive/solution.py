class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_bounds = {}
        column_bounds = {}

        for x, y in buildings:
            if x in row_bounds:
                row_bounds[x][0] = min(row_bounds[x][0], y)
                row_bounds[x][1] = max(row_bounds[x][1], y)
            else:
                row_bounds[x] = [y, y]

            if y in column_bounds:
                column_bounds[y][0] = min(column_bounds[y][0], x)
                column_bounds[y][1] = max(column_bounds[y][1], x)
            else:
                column_bounds[y] = [x, x]

        return sum(
            row_bounds[x][0] < y < row_bounds[x][1] and column_bounds[y][0] < x < column_bounds[y][1]
            for x, y in buildings
        )
