from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for value in nums:
            if value in seen:
                return value
            seen.add(value)
        raise ValueError("input does not contain the promised repeated value")
