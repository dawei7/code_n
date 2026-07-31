from functools import lru_cache


MOD = 10**9 + 7


def solve(low: str, high: str) -> int:
    def count_at_most(bound: str) -> int:
        @lru_cache(None)
        def dp(index: int, previous: int, started: bool, tight: bool) -> int:
            if index == len(bound):
                return int(started)

            limit = int(bound[index]) if tight else 9
            total = 0
            for digit in range(limit + 1):
                next_tight = tight and digit == int(bound[index])
                if not started and digit == 0:
                    total += dp(index + 1, -1, False, next_tight)
                elif not started or abs(digit - previous) == 1:
                    total += dp(index + 1, digit, True, next_tight)
            return total % MOD

        return dp(0, -1, False, True)

    def decrement(value: str) -> str:
        digits = list(value)
        index = len(digits) - 1
        while digits[index] == "0":
            digits[index] = "9"
            index -= 1
        digits[index] = str(int(digits[index]) - 1)
        result = "".join(digits).lstrip("0")
        return result or "0"

    return (count_at_most(high) - count_at_most(decrement(low))) % MOD
