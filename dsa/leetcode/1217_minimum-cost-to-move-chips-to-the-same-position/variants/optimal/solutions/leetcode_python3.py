from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_count = sum(value % 2 for value in position)
        even_count = len(position) - odd_count
        return min(odd_count, even_count)
