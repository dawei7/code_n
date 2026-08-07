from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        nearest = [-1] * 30
        answer = [1] * len(nums)

        for index in range(len(nums) - 1, -1, -1):
            for bit in range(30):
                if nums[index] & (1 << bit):
                    nearest[bit] = index

            furthest = index
            for position in nearest:
                furthest = max(furthest, position)
            answer[index] = furthest - index + 1

        return answer
