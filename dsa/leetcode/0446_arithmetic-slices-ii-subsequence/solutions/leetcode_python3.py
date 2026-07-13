from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        endings = [{} for _ in nums]
        answer = 0

        for right in range(len(nums)):
            for left in range(right):
                difference = nums[right] - nums[left]
                extensions = endings[left].get(difference, 0)
                answer += extensions
                endings[right][difference] = endings[right].get(difference, 0) + extensions + 1
        return answer
