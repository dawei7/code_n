from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arranged = [0] * len(nums)
        positive_index = 0
        negative_index = 1

        for value in nums:
            if value > 0:
                arranged[positive_index] = value
                positive_index += 2
            else:
                arranged[negative_index] = value
                negative_index += 2

        return arranged
