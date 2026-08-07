from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        frequencies = defaultdict(int)
        pairs = 0
        left = 0
        answer = 0

        for right, value in enumerate(nums):
            pairs += frequencies[value]
            frequencies[value] += 1

            while pairs >= k:
                answer += len(nums) - right
                outgoing = nums[left]
                frequencies[outgoing] -= 1
                pairs -= frequencies[outgoing]
                left += 1

        return answer
