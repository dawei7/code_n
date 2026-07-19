from functools import reduce
from operator import or_
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = reduce(or_, nums)

        def count(index: int, current: int) -> int:
            if current == target:
                return 1 << (len(nums) - index)
            if index == len(nums):
                return 0

            return count(index + 1, current) + count(
                index + 1, current | nums[index]
            )

        return count(0, 0)
