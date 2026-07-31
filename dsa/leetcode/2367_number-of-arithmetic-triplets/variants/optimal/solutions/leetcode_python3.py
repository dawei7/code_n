from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        values = set(nums)
        return sum(
            value - diff in values and value - 2 * diff in values
            for value in nums
        )
