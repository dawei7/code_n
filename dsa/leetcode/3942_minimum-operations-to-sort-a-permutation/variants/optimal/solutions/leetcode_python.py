from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        zero_index = nums.index(0)

        cyclic_increasing = all(
            nums[(index + 1) % length] == (nums[index] + 1) % length
            for index in range(length)
        )
        if cyclic_increasing:
            return min(zero_index, length - zero_index + 2)

        cyclic_decreasing = all(
            nums[(index + 1) % length] == (nums[index] - 1) % length
            for index in range(length)
        )
        if cyclic_decreasing:
            return min(length - zero_index, zero_index + 2)

        return -1
