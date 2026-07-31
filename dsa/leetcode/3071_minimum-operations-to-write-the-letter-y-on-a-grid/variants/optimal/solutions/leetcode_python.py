class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        middle = n // 2
        counts = [[0, 0, 0], [0, 0, 0]]

        for row in range(n):
            for column in range(n):
                belongs_to_y = (row <= middle and (column == row or column == n - 1 - row)) or (
                    row >= middle and column == middle
                )
                counts[belongs_to_y][grid[row][column]] += 1

        return min(
            n * n - counts[True][y_value] - counts[False][background_value]
            for y_value in range(3)
            for background_value in range(3)
            if y_value != background_value
        )
