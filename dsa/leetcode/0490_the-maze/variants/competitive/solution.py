from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        left_stop = [[-1] * cols for _ in range(rows)]
        right_stop = [[-1] * cols for _ in range(rows)]
        top_stop = [[-1] * cols for _ in range(rows)]
        bottom_stop = [[-1] * cols for _ in range(rows)]

        for row in range(rows):
            col = 0
            while col < cols:
                if maze[row][col] == 1:
                    col += 1
                    continue
                segment_start = col
                while col < cols and maze[row][col] == 0:
                    col += 1
                segment_end = col - 1
                for member in range(segment_start, col):
                    left_stop[row][member] = segment_start
                    right_stop[row][member] = segment_end

        for col in range(cols):
            row = 0
            while row < rows:
                if maze[row][col] == 1:
                    row += 1
                    continue
                segment_start = row
                while row < rows and maze[row][col] == 0:
                    row += 1
                segment_end = row - 1
                for member in range(segment_start, row):
                    top_stop[member][col] = segment_start
                    bottom_stop[member][col] = segment_end

        start_cell = (start[0], start[1])
        target = (destination[0], destination[1])
        queue = deque([start_cell])
        visited = {start_cell}

        while queue:
            row, col = queue.popleft()
            if (row, col) == target:
                return True
            neighbors = (
                (row, left_stop[row][col]),
                (row, right_stop[row][col]),
                (top_stop[row][col], col),
                (bottom_stop[row][col], col),
            )
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False
