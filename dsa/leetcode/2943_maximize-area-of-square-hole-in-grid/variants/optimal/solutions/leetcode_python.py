from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def maximum_opening(bars: List[int]) -> int:
            removable = set(bars)
            longest_run = 0

            for bar in removable:
                if bar - 1 in removable:
                    continue
                run = 1
                while bar + run in removable:
                    run += 1
                longest_run = max(longest_run, run)

            return longest_run + 1

        side = min(maximum_opening(hBars), maximum_opening(vBars))
        return side * side
