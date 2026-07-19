from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        first_island = []

        for start_row in range(n):
            if first_island:
                break
            for start_col in range(n):
                if grid[start_row][start_col] != 1:
                    continue
                stack = [(start_row, start_col)]
                visited[start_row][start_col] = True
                while stack:
                    row, col = stack.pop()
                    first_island.append((row, col))
                    for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = row + row_step
                        next_col = col + col_step
                        if (
                            0 <= next_row < n
                            and 0 <= next_col < n
                            and not visited[next_row][next_col]
                            and grid[next_row][next_col] == 1
                        ):
                            visited[next_row][next_col] = True
                            stack.append((next_row, next_col))
                break

        queue = deque(first_island)
        distance = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for row_step, col_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + row_step
                    next_col = col + col_step
                    if not (0 <= next_row < n and 0 <= next_col < n):
                        continue
                    if visited[next_row][next_col]:
                        continue
                    if grid[next_row][next_col] == 1:
                        return distance
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))
            distance += 1
        return -1
