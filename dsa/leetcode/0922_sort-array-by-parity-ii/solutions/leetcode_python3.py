from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_index = 0
        odd_index = 1

        while even_index < len(nums):
            if nums[even_index] % 2:
                while nums[odd_index] % 2:
                    odd_index += 2
                nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
            even_index += 2

        return nums

