from math import isqrt
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = isqrt(area)
        while area % width != 0:
            width -= 1
        return [area // width, width]
