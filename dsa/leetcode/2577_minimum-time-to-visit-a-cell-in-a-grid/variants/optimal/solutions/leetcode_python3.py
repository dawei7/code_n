from heapq import heappop, heappush


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        infinity = 10**18
        earliest = [[infinity] * cols for _ in range(rows)]
        earliest[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            time, row, col = heappop(heap)
            if time != earliest[row][col]:
                continue
            if row == rows - 1 and col == cols - 1:
                return time

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row, next_col = row + dr, col + dc
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue

                next_time = time + 1
                required = grid[next_row][next_col]
                if next_time < required:
                    next_time = required + ((required - next_time) & 1)

                if next_time < earliest[next_row][next_col]:
                    earliest[next_row][next_col] = next_time
                    heappush(heap, (next_time, next_row, next_col))

        return -1
