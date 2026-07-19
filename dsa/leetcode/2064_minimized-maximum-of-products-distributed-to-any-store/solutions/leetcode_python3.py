from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low = 1
        high = max(quantities)

        while low < high:
            limit = (low + high) // 2
            stores_needed = sum(
                (quantity + limit - 1) // limit for quantity in quantities
            )
            if stores_needed <= n:
                high = limit
            else:
                low = limit + 1

        return low
