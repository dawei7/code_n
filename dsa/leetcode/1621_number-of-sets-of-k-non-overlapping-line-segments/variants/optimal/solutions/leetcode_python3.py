class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        modulus = 1_000_000_007
        upper = n + k - 1
        choose = 2 * k
        numerator = 1
        denominator = 1
        for offset in range(1, choose + 1):
            numerator = numerator * (upper - choose + offset) % modulus
            denominator = denominator * offset % modulus
        return numerator * pow(denominator, modulus - 2, modulus) % modulus
