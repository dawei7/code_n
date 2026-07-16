from typing import List, Optional, Tuple


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        land_count = sum(sum(row) for row in grid)

        if land_count == 0:
            return 0

        discovery = [[-1] * columns for _ in range(rows)]
        low = [[-1] * columns for _ in range(rows)]
        time = 0
        visited = 0
        has_articulation = False

        def dfs(
            row: int,
            column: int,
            parent: Optional[Tuple[int, int]],
        ) -> None:
            nonlocal time, visited, has_articulation

            discovery[row][column] = time
            low[row][column] = time
            time += 1
            visited += 1
            children = 0

            for row_delta, column_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_delta
                next_column = column + column_delta

                if not (0 <= next_row < rows and 0 <= next_column < columns):
                    continue
                if grid[next_row][next_column] == 0:
                    continue
                if (next_row, next_column) == parent:
                    continue

                if discovery[next_row][next_column] == -1:
                    children += 1
                    dfs(next_row, next_column, (row, column))
                    low[row][column] = min(
                        low[row][column], low[next_row][next_column]
                    )

                    if parent is None and children > 1:
                        has_articulation = True
                    if (
                        parent is not None
                        and low[next_row][next_column] >= discovery[row][column]
                    ):
                        has_articulation = True
                else:
                    low[row][column] = min(
                        low[row][column], discovery[next_row][next_column]
                    )

        start = next(
            (row, column)
            for row in range(rows)
            for column in range(columns)
            if grid[row][column] == 1
        )
        dfs(start[0], start[1], None)

        if visited != land_count:
            return 0
        if land_count == 1:
            return 1
        return 1 if has_articulation else 2
