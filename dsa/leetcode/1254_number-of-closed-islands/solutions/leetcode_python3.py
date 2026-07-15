from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        answer = 0
        for start_row in range(rows):
            for start_column in range(columns):
                if grid[start_row][start_column] != 0:
                    continue
                grid[start_row][start_column] = 1
                stack = [(start_row, start_column)]
                closed = True
                while stack:
                    row, column = stack.pop()
                    if row in (0, rows - 1) or column in (0, columns - 1):
                        closed = False
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = row + dr, column + dc
                        if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            stack.append((nr, nc))
                answer += closed
        return answer
