from math import isqrt


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        limit = isqrt(n)

        for divisor in range(1, limit + 1):
            if n % divisor == 0:
                k -= 1
                if k == 0:
                    return divisor

        for divisor in range(limit, 0, -1):
            if n % divisor != 0:
                continue
            quotient = n // divisor
            if quotient == divisor:
                continue
            k -= 1
            if k == 0:
                return quotient

        return -1

