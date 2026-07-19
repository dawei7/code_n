from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = {}
        pairs = 0

        for value in nums:
            pairs += seen.get(value - k, 0)
            pairs += seen.get(value + k, 0)
            seen[value] = seen.get(value, 0) + 1

        return pairs
