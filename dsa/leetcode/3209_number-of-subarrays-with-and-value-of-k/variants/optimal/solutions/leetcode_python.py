from collections import defaultdict
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ending_counts: dict[int, int] = {}
        answer = 0
        for number in nums:
            next_counts: dict[int, int] = defaultdict(int)
            next_counts[number] += 1
            for value, count in ending_counts.items():
                next_counts[value & number] += count
            answer += next_counts.get(k, 0)
            ending_counts = next_counts
        return answer
