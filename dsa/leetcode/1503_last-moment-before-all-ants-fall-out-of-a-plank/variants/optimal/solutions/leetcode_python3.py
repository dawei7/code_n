from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        last_left = max(left, default=0)
        last_right = n - min(right, default=n)
        return max(last_left, last_right)
