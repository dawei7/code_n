from collections import deque
from typing import List


def _shortest_distance(grid: List[List[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    distance_sum = [[0] * columns for _ in range(rows)]
    reach_count = [[0] * columns for _ in range(rows)]
    buildings = 0

    for start_row in range(rows):
        for start_column in range(columns):
            if grid[start_row][start_column] != 1:
                continue
            buildings += 1
            visited = [[False] * columns for _ in range(rows)]
            queue = deque([(start_row, start_column, 0)])

            while queue:
                row, column, distance = queue.popleft()
                for next_row, next_column in (
                    (row - 1, column),
                    (row + 1, column),
                    (row, column - 1),
                    (row, column + 1),
                ):
                    if not (0 <= next_row < rows and 0 <= next_column < columns):
                        continue
                    if visited[next_row][next_column] or grid[next_row][next_column] != 0:
                        continue
                    visited[next_row][next_column] = True
                    next_distance = distance + 1
                    distance_sum[next_row][next_column] += next_distance
                    reach_count[next_row][next_column] += 1
                    queue.append((next_row, next_column, next_distance))

    best = min(
        (
            distance_sum[row][column]
            for row in range(rows)
            for column in range(columns)
            if grid[row][column] == 0 and reach_count[row][column] == buildings
        ),
        default=None,
    )
    return -1 if best is None else best


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        return _shortest_distance(grid)
