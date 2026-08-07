from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        present = set(nums)
        candidate = max(1, sum(nums) // len(nums) + 1)
        while candidate in present:
            candidate += 1
        return candidate
