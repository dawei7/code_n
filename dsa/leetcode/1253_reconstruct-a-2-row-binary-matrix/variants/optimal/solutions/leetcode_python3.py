from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        top = [0] * len(colsum)
        bottom = [0] * len(colsum)
        for index, value in enumerate(colsum):
            if value == 2:
                top[index] = bottom[index] = 1
                upper -= 1
                lower -= 1
        if upper < 0 or lower < 0:
            return []
        for index, value in enumerate(colsum):
            if value == 1:
                if upper > lower:
                    top[index] = 1
                    upper -= 1
                else:
                    bottom[index] = 1
                    lower -= 1
        return [top, bottom] if upper == 0 and lower == 0 else []
