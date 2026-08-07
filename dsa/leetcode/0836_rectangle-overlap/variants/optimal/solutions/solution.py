from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        horizontal = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        vertical = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        return horizontal and vertical
