from math import isqrt
from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return (isqrt(8 * len(grades) + 1) - 1) // 2
