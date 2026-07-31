from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def capped_sum(cap: int) -> int:
            return sum(min(value, cap) for value in arr)

        low, high = 0, max(arr)
        while low < high:
            middle = (low + high) // 2
            if capped_sum(middle) < target:
                low = middle + 1
            else:
                high = middle

        upper = low
        lower = upper - 1
        if abs(capped_sum(lower) - target) <= abs(capped_sum(upper) - target):
            return lower
        return upper
