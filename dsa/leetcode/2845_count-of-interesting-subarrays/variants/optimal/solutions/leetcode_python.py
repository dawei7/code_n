from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        remainder_counts = defaultdict(int)
        remainder_counts[0] = 1
        qualifying_prefix = 0
        answer = 0

        for value in nums:
            qualifying_prefix += value % modulo == k
            remainder = qualifying_prefix % modulo
            answer += remainder_counts[(remainder - k) % modulo]
            remainder_counts[remainder] += 1

        return answer
