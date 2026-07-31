from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        prefix = [0] * len(pattern)
        matched = 0

        for index in range(1, len(pattern)):
            while matched and pattern[index] != pattern[matched]:
                matched = prefix[matched - 1]
            if pattern[index] == pattern[matched]:
                matched += 1
            prefix[index] = matched

        answer = 0
        matched = 0

        for index in range(len(nums) - 1):
            relation = (nums[index + 1] > nums[index]) - (
                nums[index + 1] < nums[index]
            )
            while matched and relation != pattern[matched]:
                matched = prefix[matched - 1]
            if relation == pattern[matched]:
                matched += 1
            if matched == len(pattern):
                answer += 1
                matched = prefix[matched - 1]

        return answer
