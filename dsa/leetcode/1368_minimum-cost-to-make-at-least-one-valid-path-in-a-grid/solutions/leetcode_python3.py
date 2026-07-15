from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        rows, cols = len(grid), len(grid[0])
        distance = [[10**9] * cols for _ in range(rows)]
        distance[0][0] = 0
        queue = deque([(0, 0)])

        while queue:
            row, col = queue.popleft()
            for code, (dr, dc) in enumerate(directions, start=1):
                next_row, next_col = row + dr, col + dc
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue
                weight = 0 if grid[row][col] == code else 1
                candidate = distance[row][col] + weight
                if candidate >= distance[next_row][next_col]:
                    continue
                distance[next_row][next_col] = candidate
                if weight == 0:
                    queue.appendleft((next_row, next_col))
                else:
                    queue.append((next_row, next_col))

        return distance[-1][-1]
