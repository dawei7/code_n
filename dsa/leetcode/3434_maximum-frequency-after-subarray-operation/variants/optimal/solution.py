from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        base = nums.count(k)
        best_gain = 0

        for source in range(1, 51):
            if source == k:
                continue
            current = 0
            for value in nums:
                if value == source:
                    current += 1
                elif value == k:
                    current -= 1
                current = max(0, current)
                best_gain = max(best_gain, current)

        return base + best_gain
