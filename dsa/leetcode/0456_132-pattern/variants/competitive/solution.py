from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        middle = float("-inf")
        for value in reversed(nums):
            if value < middle:
                return True
            while stack and value > stack[-1]:
                middle = stack.pop()
            stack.append(value)
        return False
