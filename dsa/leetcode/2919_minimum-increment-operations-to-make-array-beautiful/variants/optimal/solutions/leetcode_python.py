from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        third_last = 0
        second_last = 0
        last = 0

        for value in nums:
            current = max(0, k - value) + min(third_last, second_last, last)
            third_last, second_last, last = second_last, last, current

        return min(third_last, second_last, last)
