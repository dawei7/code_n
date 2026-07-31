class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        reachable = set(range(rows))

        for column in range(1, len(grid[0])):
            next_rows = set()
            for row in range(rows):
                for previous_row in (row - 1, row, row + 1):
                    if (
                        previous_row in reachable
                        and 0 <= previous_row < rows
                        and grid[row][column] > grid[previous_row][column - 1]
                    ):
                        next_rows.add(row)
                        break
            if not next_rows:
                return column - 1
            reachable = next_rows

        return len(grid[0]) - 1
