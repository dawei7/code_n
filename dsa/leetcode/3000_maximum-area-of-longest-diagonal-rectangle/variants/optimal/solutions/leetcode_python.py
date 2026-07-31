from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        best_diagonal = 0
        best_area = 0

        for length, width in dimensions:
            diagonal = length * length + width * width
            area = length * width
            if diagonal > best_diagonal or (
                diagonal == best_diagonal and area > best_area
            ):
                best_diagonal = diagonal
                best_area = area

        return best_area
