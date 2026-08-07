from typing import List


class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        non_negative = [value for value in nums if value >= 0]
        if not non_negative:
            return nums

        shift = k % len(non_negative)
        rotated = non_negative[shift:] + non_negative[:shift]

        result = nums[:]
        next_value = 0
        for index, value in enumerate(nums):
            if value >= 0:
                result[index] = rotated[next_value]
                next_value += 1

        return result
