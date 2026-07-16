from functools import cache


def solve(n):
    @cache
    def days(oranges):
        if oranges <= 1:
            return oranges
        return 1 + min(
            oranges % 2 + days(oranges // 2),
            oranges % 3 + days(oranges // 3),
        )

    return days(n)

