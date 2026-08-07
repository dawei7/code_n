from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for value, frequency in frequencies.items():
            buckets[frequency].append(value)

        result = []
        for frequency in range(len(nums), 0, -1):
            for value in buckets[frequency]:
                result.append(value)
                if len(result) == k:
                    return result
        return result
