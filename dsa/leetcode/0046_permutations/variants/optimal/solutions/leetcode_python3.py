from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def arrange(first: int) -> None:
            if first == len(nums):
                result.append(nums[:])
                return
            for index in range(first, len(nums)):
                nums[first], nums[index] = nums[index], nums[first]
                arrange(first + 1)
                nums[first], nums[index] = nums[index], nums[first]

        arrange(0)
        return result
