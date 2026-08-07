from typing import List


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        values = sorted(nums)
        prefix = [0]
        for value in values:
            prefix.append(prefix[-1] + value)

        left = 0
        best = 1
        for right in range(len(values)):
            while self._cost(values, prefix, left, right) > k:
                left += 1
            best = max(best, right - left + 1)
        return best

    def _cost(self, values: List[int], prefix: List[int], left: int, right: int) -> int:
        middle = (left + right) // 2
        median = values[middle]
        left_cost = median * (middle - left) - (prefix[middle] - prefix[left])
        right_cost = prefix[right + 1] - prefix[middle + 1] - median * (right - middle)
        return left_cost + right_cost
