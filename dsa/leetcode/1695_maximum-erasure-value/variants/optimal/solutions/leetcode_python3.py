from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        present = set()
        left = 0
        current_sum = 0
        best = 0

        for value in nums:
            while value in present:
                removed = nums[left]
                present.remove(removed)
                current_sum -= removed
                left += 1
            present.add(value)
            current_sum += value
            best = max(best, current_sum)

        return best
