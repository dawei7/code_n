from typing import List


class Solution:
    def findIndices(
        self,
        nums: List[int],
        indexDifference: int,
        valueDifference: int,
    ) -> List[int]:
        minimum_index = 0
        maximum_index = 0

        for right in range(indexDifference, len(nums)):
            eligible = right - indexDifference
            if nums[eligible] < nums[minimum_index]:
                minimum_index = eligible
            if nums[eligible] > nums[maximum_index]:
                maximum_index = eligible

            if nums[right] - nums[minimum_index] >= valueDifference:
                return [minimum_index, right]
            if nums[maximum_index] - nums[right] >= valueDifference:
                return [maximum_index, right]

        return [-1, -1]
