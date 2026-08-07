from heapq import heappop, heappush


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows = len(moveTime)
        columns = len(moveTime[0])
        distances = [[float("inf")] * columns for _ in range(rows)]
        distances[0][0] = 0
        queue = [(0, 0, 0)]

        while queue:
            time, row, column = heappop(queue)

            if time != distances[row][column]:
                continue
            if row == rows - 1 and column == columns - 1:
                return time

            for row_delta, column_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_delta
                next_column = column + column_delta

                if 0 <= next_row < rows and 0 <= next_column < columns:
                    next_time = max(time, moveTime[next_row][next_column]) + 1
                    if next_time < distances[next_row][next_column]:
                        distances[next_row][next_column] = next_time
                        heappush(queue, (next_time, next_row, next_column))

        return -1
