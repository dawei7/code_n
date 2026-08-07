from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        answer = []

        for start in range(0, len(nums), 3):
            if nums[start + 2] - nums[start] > k:
                return []
            answer.append(nums[start : start + 3])

        return answer
