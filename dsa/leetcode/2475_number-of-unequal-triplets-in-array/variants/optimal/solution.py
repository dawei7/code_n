from collections import Counter
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        answer = 0
        left = 0
        right = len(nums)

        for count in Counter(nums).values():
            right -= count
            answer += left * count * right
            left += count

        return answer
