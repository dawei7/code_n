from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        total = sum(amount)
        return max(max(amount), (total + 1) // 2)
