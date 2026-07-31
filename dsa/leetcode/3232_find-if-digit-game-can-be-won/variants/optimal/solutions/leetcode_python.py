from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        balance = 0
        for value in nums:
            balance += value if value < 10 else -value
        return balance != 0
