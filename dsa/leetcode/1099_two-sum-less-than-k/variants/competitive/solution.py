from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        values = sorted(nums)
        left = 0
        right = len(values) - 1
        best = -1

        while left < right:
            pair_sum = values[left] + values[right]
            if pair_sum < k:
                best = max(best, pair_sum)
                left += 1
            else:
                right -= 1
        return best
