from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = Counter(nums)
        longest = 0

        for value, frequency in counts.items():
            if value + 1 in counts:
                longest = max(
                    longest,
                    frequency + counts[value + 1],
                )

        return longest

