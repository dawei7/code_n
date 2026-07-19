class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        modulus = 1_000_000_007
        if primeFactors <= 3:
            return primeFactors

        threes, remainder = divmod(primeFactors, 3)
        if remainder == 0:
            return pow(3, threes, modulus)
        if remainder == 1:
            return pow(3, threes - 1, modulus) * 4 % modulus
        return pow(3, threes, modulus) * 2 % modulus
