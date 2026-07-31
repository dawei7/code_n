class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            remaining = n
            factor_sum = 0
            factor = 2

            while factor * factor <= remaining:
                while remaining % factor == 0:
                    factor_sum += factor
                    remaining //= factor
                factor += 1

            if remaining > 1:
                factor_sum += remaining

            if factor_sum == n:
                return n
            n = factor_sum
