from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        present = set(nums)
        candidate = k
        while candidate in present:
            candidate += k
        return candidate
