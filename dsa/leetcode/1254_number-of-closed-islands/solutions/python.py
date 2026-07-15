from typing import List


def solve(grid: List[List[int]]) -> int:
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
                for row_delta, column_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + row_delta
                    next_column = column + column_delta
                    if 0 <= next_row < rows and 0 <= next_column < columns and grid[next_row][next_column] == 0:
                        grid[next_row][next_column] = 1
                        stack.append((next_row, next_column))
            answer += closed
    return answer
