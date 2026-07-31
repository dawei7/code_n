from collections import deque
from typing import List


def solve(grid: List[List[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    distance = [[float("inf")] * columns for _ in range(rows)]
    distance[0][0] = 0
    queue = deque([(0, 0)])

    while queue:
        row, column = queue.popleft()
        current = distance[row][column]

        for row_step, column_step in (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ):
            next_row = row + row_step
            next_column = column + column_step
            if not (0 <= next_row < rows and 0 <= next_column < columns):
                continue

            weight = grid[next_row][next_column]
            candidate = current + weight
            if candidate >= distance[next_row][next_column]:
                continue

            distance[next_row][next_column] = candidate
            if weight == 0:
                queue.appendleft((next_row, next_column))
            else:
                queue.append((next_row, next_column))

    return distance[rows - 1][columns - 1]
