from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        unresolved = []
        answer = 0

        for current, value in enumerate(nums):
            while unresolved and nums[unresolved[-1]] > value:
                start = unresolved.pop()
                answer += current - start
            unresolved.append(current)

        length = len(nums)
        while unresolved:
            answer += length - unresolved.pop()
        return answer
