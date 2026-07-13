from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])

        def reverse_reachable(starts):
            reached = set(starts)
            queue = deque(starts)
            while queue:
                row, column = queue.popleft()
                for row_delta, column_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + row_delta
                    next_column = column + column_delta
                    next_cell = (next_row, next_column)
                    if (
                        0 <= next_row < rows
                        and 0 <= next_column < columns
                        and next_cell not in reached
                        and heights[next_row][next_column] >= heights[row][column]
                    ):
                        reached.add(next_cell)
                        queue.append(next_cell)
            return reached

        pacific_starts = {(0, column) for column in range(columns)}
        pacific_starts.update((row, 0) for row in range(rows))
        atlantic_starts = {(rows - 1, column) for column in range(columns)}
        atlantic_starts.update((row, columns - 1) for row in range(rows))

        both = reverse_reachable(pacific_starts) & reverse_reachable(atlantic_starts)
        return [[row, column] for row in range(rows) for column in range(columns) if (row, column) in both]
