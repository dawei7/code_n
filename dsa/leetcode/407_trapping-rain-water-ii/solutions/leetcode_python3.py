from heapq import heappop, heappush


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows = len(heightMap)
        columns = len(heightMap[0])
        if rows < 3 or columns < 3:
            return 0

        visited = [[False] * columns for _ in range(rows)]
        frontier = []

        for row in range(rows):
            for column in range(columns):
                if row in (0, rows - 1) or column in (0, columns - 1):
                    visited[row][column] = True
                    heappush(frontier, (heightMap[row][column], row, column))

        trapped = 0
        while frontier:
            wall, row, column = heappop(frontier)
            for row_delta, column_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_delta
                next_column = column + column_delta
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and not visited[next_row][next_column]
                ):
                    visited[next_row][next_column] = True
                    terrain = heightMap[next_row][next_column]
                    trapped += max(0, wall - terrain)
                    heappush(frontier, (max(wall, terrain), next_row, next_column))

        return trapped
