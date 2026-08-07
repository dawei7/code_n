from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for write in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                answer[write] = nums[left] * nums[left]
                left += 1
            else:
                answer[write] = nums[right] * nums[right]
                right -= 1

        return answer
