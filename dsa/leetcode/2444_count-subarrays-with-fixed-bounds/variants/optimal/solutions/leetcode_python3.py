from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_invalid = -1
        last_minimum = -1
        last_maximum = -1
        answer = 0

        for index, value in enumerate(nums):
            if value < minK or value > maxK:
                last_invalid = index
            if value == minK:
                last_minimum = index
            if value == maxK:
                last_maximum = index

            answer += max(0, min(last_minimum, last_maximum) - last_invalid)

        return answer
