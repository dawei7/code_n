from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for number in nums:
            marker = abs(number) - 1
            nums[marker] = -abs(nums[marker])
        return [index + 1 for index, marker in enumerate(nums) if marker > 0]
