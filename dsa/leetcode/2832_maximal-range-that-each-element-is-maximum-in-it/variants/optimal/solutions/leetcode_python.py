from typing import List


class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        stack = []
        for index, value in enumerate(nums):
            while stack and nums[stack[-1]] < value:
                stack.pop()
            left_boundary = stack[-1] + 1 if stack else 0
            answer[index] = index - left_boundary + 1
            stack.append(index)

        stack.clear()
        for index in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[index]:
                stack.pop()
            right_boundary = stack[-1] - 1 if stack else n - 1
            answer[index] += right_boundary - index
            stack.append(index)

        return answer
