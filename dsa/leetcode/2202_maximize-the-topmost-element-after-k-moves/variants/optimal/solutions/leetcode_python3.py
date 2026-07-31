from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        if len(nums) == 1:
            return nums[0] if k % 2 == 0 else -1

        answer = -1
        restored_count = min(len(nums), k - 1)
        if restored_count > 0:
            answer = max(nums[:restored_count])
        if k < len(nums):
            answer = max(answer, nums[k])
        return answer
