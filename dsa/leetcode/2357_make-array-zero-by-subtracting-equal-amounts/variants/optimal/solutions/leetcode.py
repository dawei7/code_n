from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len({value for value in nums if value > 0})
