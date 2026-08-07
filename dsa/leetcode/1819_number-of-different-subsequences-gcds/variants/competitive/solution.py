from math import gcd
from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        maximum = max(nums)
        present = [False] * (maximum + 1)
        for value in nums:
            present[value] = True

        answer = 0
        for candidate in range(1, maximum + 1):
            current = 0
            for multiple in range(candidate, maximum + 1, candidate):
                if present[multiple]:
                    current = gcd(current, multiple)
                    if current == candidate:
                        answer += 1
                        break
        return answer
