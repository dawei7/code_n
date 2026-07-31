from collections import deque
from heapq import heappop, heappush

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distance = [[-1] * n for _ in range(n)]
        queue = deque()
        for row in range(n):
            for column in range(n):
                if grid[row][column] == 1:
                    distance[row][column] = 0
                    queue.append((row, column))
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            row, column = queue.popleft()
            for dr, dc in directions:
                next_row, next_column = row + dr, column + dc
                if 0 <= next_row < n and 0 <= next_column < n and distance[next_row][next_column] == -1:
                    distance[next_row][next_column] = distance[row][column] + 1
                    queue.append((next_row, next_column))
        best = [[-1] * n for _ in range(n)]
        best[0][0] = distance[0][0]
        heap = [(-distance[0][0], 0, 0)]
        while heap:
            negative_safety, row, column = heappop(heap)
            safety = -negative_safety
            if safety < best[row][column]:
                continue
            if row == n - 1 and column == n - 1:
                return safety
            for dr, dc in directions:
                next_row, next_column = row + dr, column + dc
                if 0 <= next_row < n and 0 <= next_column < n:
                    candidate = min(safety, distance[next_row][next_column])
                    if candidate > best[next_row][next_column]:
                        best[next_row][next_column] = candidate
                        heappush(heap, (-candidate, next_row, next_column))
        return 0
