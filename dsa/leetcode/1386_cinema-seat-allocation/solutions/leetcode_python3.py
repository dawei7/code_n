from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(
        self,
        n: int,
        reservedSeats: List[List[int]],
    ) -> int:
        occupied = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                occupied[row] |= 1 << seat

        left_block = sum(1 << seat for seat in range(2, 6))
        middle_block = sum(1 << seat for seat in range(4, 8))
        right_block = sum(1 << seat for seat in range(6, 10))

        families = 2 * (n - len(occupied))
        for mask in occupied.values():
            left_free = mask & left_block == 0
            right_free = mask & right_block == 0
            if left_free and right_free:
                families += 2
            elif left_free or right_free or mask & middle_block == 0:
                families += 1

        return families
