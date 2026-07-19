from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        removals = len(nums) - k

        for value in nums:
            while removals and stack and stack[-1] > value:
                stack.pop()
                removals -= 1
            if len(stack) < k:
                stack.append(value)
            else:
                removals -= 1

        return stack
