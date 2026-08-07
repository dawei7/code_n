class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        while n > 0:
            n //= 5
            zeroes += n
        return zeroes
