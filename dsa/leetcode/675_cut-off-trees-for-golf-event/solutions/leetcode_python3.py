from collections import deque


class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        rows = len(forest)
        columns = len(forest[0])
        trees = sorted(
            (forest[row][column], row, column)
            for row in range(rows)
            for column in range(columns)
            if forest[row][column] > 1
        )
        if trees and forest[0][0] == 0:
            return -1

        def distance(start_row, start_column, target_row, target_column):
            if (start_row, start_column) == (target_row, target_column):
                return 0
            queue = deque([(start_row, start_column, 0)])
            visited = {(start_row, start_column)}
            while queue:
                row, column, steps = queue.popleft()
                for next_row, next_column in (
                    (row - 1, column),
                    (row + 1, column),
                    (row, column - 1),
                    (row, column + 1),
                ):
                    if not (0 <= next_row < rows and 0 <= next_column < columns):
                        continue
                    if forest[next_row][next_column] == 0:
                        continue
                    if (next_row, next_column) in visited:
                        continue
                    if (next_row, next_column) == (target_row, target_column):
                        return steps + 1
                    visited.add((next_row, next_column))
                    queue.append((next_row, next_column, steps + 1))
            return -1

        row = column = total = 0
        for _, target_row, target_column in trees:
            steps = distance(row, column, target_row, target_column)
            if steps == -1:
                return -1
            total += steps
            row, column = target_row, target_column
        return total
