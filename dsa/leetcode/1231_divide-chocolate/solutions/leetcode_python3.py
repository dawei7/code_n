from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        pieces_needed = k + 1
        low = min(sweetness)
        high = sum(sweetness) // pieces_needed

        while low < high:
            candidate = (low + high + 1) // 2
            pieces = 0
            current = 0
            for value in sweetness:
                current += value
                if current >= candidate:
                    pieces += 1
                    current = 0

            if pieces >= pieces_needed:
                low = candidate
            else:
                high = candidate - 1

        return low
