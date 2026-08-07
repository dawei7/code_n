from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low = 0
        high = sum(batteries) // n

        while low < high:
            middle = (low + high + 1) // 2
            available = sum(min(capacity, middle) for capacity in batteries)
            if available >= n * middle:
                low = middle
            else:
                high = middle - 1

        return low
