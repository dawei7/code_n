class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        columns = len(grid[0])
        maximum_cost = rows + columns - 2

        if k >= maximum_cost:
            best = [-1] * columns
            for row in range(rows):
                for column in range(columns):
                    if row == 0 and column == 0:
                        best[column] = 0
                    else:
                        previous = max(
                            best[column] if row > 0 else -1,
                            best[column - 1] if column > 0 else -1,
                        )
                        best[column] = previous + grid[row][column]
            return best[-1]

        limit = min(k, maximum_cost)
        best = [[-1] * (limit + 1) for _ in range(columns)]

        for row in range(rows):
            for column in range(columns):
                value = grid[row][column]
                cell_cost = 0 if value == 0 else 1
                from_above = best[column]
                from_left = best[column - 1] if column > 0 else None
                current = [-1] * (limit + 1)

                if row == 0 and column == 0:
                    current[0] = 0
                else:
                    for used in range(cell_cost, min(limit, row + column) + 1):
                        previous_cost = used - cell_cost
                        previous = from_above[previous_cost] if row > 0 else -1
                        if from_left is not None:
                            previous = max(previous, from_left[previous_cost])
                        if previous >= 0:
                            current[used] = previous + value

                best[column] = current

        return max(best[-1])
