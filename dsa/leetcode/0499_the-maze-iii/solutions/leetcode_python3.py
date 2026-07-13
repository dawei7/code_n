from heapq import heappop, heappush
from typing import List


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        rows, cols = len(maze), len(maze[0])
        left = [[-1] * cols for _ in range(rows)]
        right = [[-1] * cols for _ in range(rows)]
        top = [[-1] * cols for _ in range(rows)]
        bottom = [[-1] * cols for _ in range(rows)]

        for row in range(rows):
            col = 0
            while col < cols:
                if maze[row][col]:
                    col += 1
                    continue
                start = col
                while col < cols and maze[row][col] == 0:
                    col += 1
                end = col - 1
                for member in range(start, col):
                    left[row][member], right[row][member] = start, end

        for col in range(cols):
            row = 0
            while row < rows:
                if maze[row][col]:
                    row += 1
                    continue
                start = row
                while row < rows and maze[row][col] == 0:
                    row += 1
                end = row - 1
                for member in range(start, row):
                    top[member][col], bottom[member][col] = start, end

        target = (hole[0], hole[1])
        start_cell = (ball[0], ball[1])
        heap = [(0, "", ball[0], ball[1])]
        best = {start_cell: (0, "")}
        while heap:
            distance, path, row, col = heappop(heap)
            if best.get((row, col)) != (distance, path):
                continue
            if (row, col) == target:
                return path
            endpoints = (("d", bottom[row][col], col), ("l", row, left[row][col]), ("r", row, right[row][col]), ("u", top[row][col], col))
            for direction, next_row, next_col in endpoints:
                if direction == "d" and col == target[1] and row < target[0] <= next_row:
                    next_row = target[0]
                elif direction == "u" and col == target[1] and next_row <= target[0] < row:
                    next_row = target[0]
                elif direction == "r" and row == target[0] and col < target[1] <= next_col:
                    next_col = target[1]
                elif direction == "l" and row == target[0] and next_col <= target[1] < col:
                    next_col = target[1]
                traveled = abs(next_row - row) + abs(next_col - col)
                candidate = (distance + traveled, path + direction)
                cell = (next_row, next_col)
                if cell not in best or candidate < best[cell]:
                    best[cell] = candidate
                    heappush(heap, (candidate[0], candidate[1], next_row, next_col))
        return "impossible"
