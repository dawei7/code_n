from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []

        for start in range(len(nums) - k + 1):
            frequency = Counter(nums[start : start + k])
            ranked = sorted(
                frequency.items(),
                key=lambda item: (item[1], item[0]),
                reverse=True,
            )
            answer.append(
                sum(value * count for value, count in ranked[:x])
            )

        return answer
