from heapq import heappop, heappush
from typing import List


class Solution:
    def shortestDistance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        rows = len(maze)
        cols = len(maze[0])
        left = [[0] * cols for _ in range(rows)]
        right = [[0] * cols for _ in range(rows)]
        up = [[0] * cols for _ in range(rows)]
        down = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                left[row][col] = left[row][col - 1] if col and maze[row][col - 1] == 0 else col
            for col in range(cols - 1, -1, -1):
                right[row][col] = right[row][col + 1] if col + 1 < cols and maze[row][col + 1] == 0 else col

        for col in range(cols):
            for row in range(rows):
                up[row][col] = up[row - 1][col] if row and maze[row - 1][col] == 0 else row
            for row in range(rows - 1, -1, -1):
                down[row][col] = down[row + 1][col] if row + 1 < rows and maze[row + 1][col] == 0 else row

        infinity = rows * cols * 2
        distances = [[infinity] * cols for _ in range(rows)]
        start_row, start_col = start
        destination_row, destination_col = destination
        distances[start_row][start_col] = 0
        heap = [(0, start_row, start_col)]

        while heap:
            distance, row, col = heappop(heap)
            if distance != distances[row][col]:
                continue
            if row == destination_row and col == destination_col:
                return distance
            for next_row, next_col in (
                (row, left[row][col]),
                (row, right[row][col]),
                (up[row][col], col),
                (down[row][col], col),
            ):
                next_distance = distance + abs(next_row - row) + abs(next_col - col)
                if next_distance < distances[next_row][next_col]:
                    distances[next_row][next_col] = next_distance
                    heappush(heap, (next_distance, next_row, next_col))

        return -1
