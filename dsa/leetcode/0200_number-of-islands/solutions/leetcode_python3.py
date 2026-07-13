from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        islands = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] != "1":
                    continue
                islands += 1
                grid[row][column] = "0"
                stack = [(row, column)]
                while stack:
                    current_row, current_column = stack.pop()
                    for next_row, next_column in ((current_row-1,current_column),(current_row+1,current_column),(current_row,current_column-1),(current_row,current_column+1)):
                        if 0 <= next_row < rows and 0 <= next_column < columns and grid[next_row][next_column] == "1":
                            grid[next_row][next_column] = "0"
                            stack.append((next_row, next_column))
        return islands
