from collections import Counter
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = Counter({0: 1})
        odd_prefix = 0
        answer = 0
        for value in nums:
            odd_prefix += value % 2
            answer += counts[odd_prefix - k]
            counts[odd_prefix] += 1
        return answer
