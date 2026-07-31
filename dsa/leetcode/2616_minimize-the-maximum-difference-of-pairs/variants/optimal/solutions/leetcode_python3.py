from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        values = sorted(nums)

        def feasible(limit: int) -> bool:
            pairs = 0
            i = 0
            while i + 1 < len(values):
                if values[i + 1] - values[i] <= limit:
                    pairs += 1
                    i += 2
                    if pairs == p:
                        return True
                else:
                    i += 1
            return False

        low = 0
        high = values[-1] - values[0]
        while low < high:
            middle = (low + high) // 2
            if feasible(middle):
                high = middle
            else:
                low = middle + 1
        return low
