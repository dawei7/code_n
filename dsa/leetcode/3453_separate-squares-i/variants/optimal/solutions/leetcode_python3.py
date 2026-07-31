from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(side * side for _, _, side in squares)
        low = min(y for _, y, _ in squares)
        high = max(y + side for _, y, side in squares)

        for _ in range(60):
            middle = (low + high) / 2.0
            area_below = 0.0
            for _, y, side in squares:
                height = min(max(middle - y, 0.0), side)
                area_below += height * side

            if area_below * 2.0 < total_area:
                low = middle
            else:
                high = middle

        return high
