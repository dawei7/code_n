from functools import cache


class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def days(oranges: int) -> int:
            if oranges <= 1:
                return oranges
            return 1 + min(
                oranges % 2 + days(oranges // 2),
                oranges % 3 + days(oranges // 3),
            )

        return days(n)

