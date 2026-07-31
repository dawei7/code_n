class Solution:
    def createGrid(self, k: int) -> list[str]:
        rows = 20
        columns = 13
        grid = [["#"] * columns for _ in range(rows)]

        for bit in range(10):
            row = 2 * bit
            column = bit
            grid[row][column] = "."
            grid[row][column + 1] = "."

            if bit < 9:
                grid[row + 1][column] = "."
                grid[row + 1][column + 1] = "."
                grid[row + 2][column + 1] = "."

            if k & (1 << bit):
                for next_column in range(column + 1, columns):
                    grid[row][next_column] = "."

        for row in range(rows):
            grid[row][columns - 1] = "."

        return ["".join(row) for row in grid]
