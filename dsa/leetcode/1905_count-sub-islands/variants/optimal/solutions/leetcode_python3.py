from typing import List


class Solution:
    def countSubIslands(
        self, grid1: List[List[int]], grid2: List[List[int]]
    ) -> int:
        rows = len(grid1)
        columns = len(grid1[0])
        sub_islands = 0

        for start_row in range(rows):
            for start_column in range(columns):
                if grid2[start_row][start_column] == 0:
                    continue

                grid2[start_row][start_column] = 0
                stack = [(start_row, start_column)]
                contained = True
                while stack:
                    row, column = stack.pop()
                    if grid1[row][column] == 0:
                        contained = False
                    for next_row, next_column in (
                        (row - 1, column),
                        (row + 1, column),
                        (row, column - 1),
                        (row, column + 1),
                    ):
                        if (
                            0 <= next_row < rows
                            and 0 <= next_column < columns
                            and grid2[next_row][next_column] == 1
                        ):
                            grid2[next_row][next_column] = 0
                            stack.append((next_row, next_column))
                sub_islands += contained

        return sub_islands
