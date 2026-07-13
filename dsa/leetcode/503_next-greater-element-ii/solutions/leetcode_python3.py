from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        answer = [-1] * size
        stack = []
        for scan_index in range(2 * size):
            index = scan_index % size
            while stack and nums[stack[-1]] < nums[index]:
                answer[stack.pop()] = nums[index]
            if scan_index < size:
                stack.append(index)
        return answer
