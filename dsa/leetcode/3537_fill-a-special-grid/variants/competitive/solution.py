class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        side = 1 << n
        grid = [[0] * side for _ in range(side)]

        def fill(
            row: int,
            column: int,
            level: int,
            start: int,
        ) -> None:
            if level == 0:
                grid[row][column] = start
                return

            half = 1 << (level - 1)
            block_size = half * half

            fill(row, column + half, level - 1, start)
            fill(
                row + half,
                column + half,
                level - 1,
                start + block_size,
            )
            fill(
                row + half,
                column,
                level - 1,
                start + 2 * block_size,
            )
            fill(
                row,
                column,
                level - 1,
                start + 3 * block_size,
            )

        fill(0, 0, n, 0)
        return grid
