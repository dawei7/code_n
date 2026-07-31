from collections import deque


class Solution:
    def minimumSeconds(self, land: List[List[str]]) -> int:
        rows, columns = len(land), len(land[0])
        flood_time = [[float("inf")] * columns for _ in range(rows)]
        flood_queue = deque()
        start = None
        for row in range(rows):
            for column in range(columns):
                if land[row][column] == "*":
                    flood_time[row][column] = 0
                    flood_queue.append((row, column))
                elif land[row][column] == "S":
                    start = (row, column)
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while flood_queue:
            row, column = flood_queue.popleft()
            for dr, dc in directions:
                next_row, next_column = row + dr, column + dc
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and land[next_row][next_column] == "."
                    and flood_time[next_row][next_column] == float("inf")
                ):
                    flood_time[next_row][next_column] = flood_time[row][column] + 1
                    flood_queue.append((next_row, next_column))
        queue = deque([(start[0], start[1], 0)])
        seen = {start}
        while queue:
            row, column, time = queue.popleft()
            for dr, dc in directions:
                next_row, next_column = row + dr, column + dc
                if not (0 <= next_row < rows and 0 <= next_column < columns):
                    continue
                if land[next_row][next_column] == "D":
                    return time + 1
                if (
                    land[next_row][next_column] == "."
                    and (next_row, next_column) not in seen
                    and time + 1 < flood_time[next_row][next_column]
                ):
                    seen.add((next_row, next_column))
                    queue.append((next_row, next_column, time + 1))
        return -1
