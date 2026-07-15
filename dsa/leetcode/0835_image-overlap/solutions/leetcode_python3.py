from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        side = len(img1)
        rows1 = [sum(value << column for column, value in enumerate(row)) for row in img1]
        rows2 = [sum(value << column for column, value in enumerate(row)) for row in img2]

        best = 0
        for row_shift in range(1 - side, side):
            row_start = max(0, -row_shift)
            row_stop = min(side, side - row_shift)

            for column_shift in range(1 - side, side):
                overlap = 0
                for row in range(row_start, row_stop):
                    shifted = (
                        rows1[row] << column_shift
                        if column_shift >= 0
                        else rows1[row] >> -column_shift
                    )
                    overlap += (shifted & rows2[row + row_shift]).bit_count()
                best = max(best, overlap)

        return best
