from collections import deque
from typing import List


def solve(grid: List[List[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    total = rows * columns
    distance = [total] * total
    distance[0] = 0
    queue = deque([0])

    while queue:
        cell = queue.popleft()
        row, column = divmod(cell, columns)
        current = distance[cell]

        for next_row, next_column in (
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1),
        ):
            if not (
                0 <= next_row < rows
                and 0 <= next_column < columns
            ):
                continue

            neighbor = next_row * columns + next_column
            weight = grid[next_row][next_column]
            candidate = current + weight
            if candidate >= distance[neighbor]:
                continue

            distance[neighbor] = candidate
            if weight:
                queue.append(neighbor)
            else:
                queue.appendleft(neighbor)

    return distance[-1]
