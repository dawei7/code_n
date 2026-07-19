from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        best_by_value = {}
        longest = 0
        for value in arr:
            best_by_value[value] = best_by_value.get(value - difference, 0) + 1
            longest = max(longest, best_by_value[value])
        return longest
