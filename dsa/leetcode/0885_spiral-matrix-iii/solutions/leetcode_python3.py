from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        result = [[rStart, cStart]]
        target = rows * cols
        if target == 1:
            return result

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        row, column = rStart, cStart
        direction = 0
        segment_length = 1

        while True:
            for _ in range(2):
                row_step, column_step = directions[direction]
                for _ in range(segment_length):
                    row += row_step
                    column += column_step
                    if 0 <= row < rows and 0 <= column < cols:
                        result.append([row, column])
                        if len(result) == target:
                            return result
                direction = (direction + 1) % 4
            segment_length += 1
