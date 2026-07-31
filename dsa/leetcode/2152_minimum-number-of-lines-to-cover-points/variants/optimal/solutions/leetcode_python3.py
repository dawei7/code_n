from functools import lru_cache
from typing import List


class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        count = len(points)
        all_covered = (1 << count) - 1
        line_masks = [[0] * count for _ in range(count)]

        for first in range(count):
            for second in range(first + 1, count):
                x1, y1 = points[first]
                x2, y2 = points[second]
                mask = 0
                for index, (x, y) in enumerate(points):
                    if (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1):
                        mask |= 1 << index
                line_masks[first][second] = mask

        @lru_cache(maxsize=None)
        def minimum_lines(covered: int) -> int:
            if covered == all_covered:
                return 0

            first = next(
                index for index in range(count) if not (covered >> index) & 1
            )
            others = [
                index
                for index in range(first + 1, count)
                if not (covered >> index) & 1
            ]
            if not others:
                return 1

            return 1 + min(
                minimum_lines(covered | line_masks[first][second])
                for second in others
            )

        return minimum_lines(0)
