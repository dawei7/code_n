from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        row_count = len(boxGrid)
        column_count = len(boxGrid[0])
        rotated = [["."] * row_count for _ in range(column_count)]

        for row in range(row_count):
            landing_column = column_count - 1
            rotated_column = row_count - 1 - row

            for column in range(column_count - 1, -1, -1):
                cell = boxGrid[row][column]
                if cell == "*":
                    rotated[column][rotated_column] = "*"
                    landing_column = column - 1
                elif cell == "#":
                    rotated[landing_column][rotated_column] = "#"
                    landing_column -= 1

        return rotated
