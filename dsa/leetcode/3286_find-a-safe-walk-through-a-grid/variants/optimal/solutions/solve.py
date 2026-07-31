from collections import deque
from typing import List


def solve(grid: List[List[int]], health: int) -> bool:
    rows = len(grid)
    columns = len(grid[0])
    distance = [[rows * columns] * columns for _ in range(rows)]
    distance[0][0] = grid[0][0]
    queue = deque([(0, 0)])

    while queue:
        row, column = queue.popleft()
        current = distance[row][column]

        for next_row, next_column in (
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1),
        ):
            if not (0 <= next_row < rows and 0 <= next_column < columns):
                continue

            candidate = current + grid[next_row][next_column]
            if candidate >= distance[next_row][next_column]:
                continue

            distance[next_row][next_column] = candidate
            if grid[next_row][next_column] == 0:
                queue.appendleft((next_row, next_column))
            else:
                queue.append((next_row, next_column))

    return distance[-1][-1] < health
