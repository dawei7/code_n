"""App-local reference solution for LeetCode 2827."""

from functools import cache


def solve(low: int, high: int, k: int) -> int:
    """Return the number of beautiful integers in the inclusive range."""

    def count(bound: int) -> int:
        if bound <= 0:
            return 0

        digits = str(bound)

        @cache
        def dp(
            position: int,
            remainder: int,
            balance: int,
            tight: bool,
            started: bool,
        ) -> int:
            if position == len(digits):
                return int(started and remainder == 0 and balance == 0)

            limit = int(digits[position]) if tight else 9
            total = 0

            for digit in range(limit + 1):
                next_tight = tight and digit == limit
                if not started and digit == 0:
                    total += dp(position + 1, 0, 0, next_tight, False)
                else:
                    next_balance = balance + (1 if digit % 2 == 0 else -1)
                    total += dp(
                        position + 1,
                        (remainder * 10 + digit) % k,
                        next_balance,
                        next_tight,
                        True,
                    )

            return total

        return dp(0, 0, 0, True, False)

    return count(high) - count(low - 1)
