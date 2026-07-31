from functools import lru_cache


class Solution:
    def rotatedDigits(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]
        valid = {0, 1, 2, 5, 6, 8, 9}
        changing = {2, 5, 6, 9}

        @lru_cache(maxsize=None)
        def count(position: int, tight: bool, changed: bool) -> int:
            if position == len(digits):
                return int(changed)
            limit = digits[position] if tight else 9
            total = 0
            for digit in range(limit + 1):
                if digit in valid:
                    total += count(
                        position + 1,
                        tight and digit == limit,
                        changed or digit in changing,
                    )
            return total

        return count(0, True, False)
