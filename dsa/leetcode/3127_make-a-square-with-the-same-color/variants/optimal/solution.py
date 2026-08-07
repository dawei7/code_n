class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for row in range(2):
            for column in range(2):
                black = sum(
                    grid[row + row_offset][column + column_offset] == "B"
                    for row_offset in range(2)
                    for column_offset in range(2)
                )
                if black != 2:
                    return True
        return False
