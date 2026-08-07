class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = 1_000_000_007
        total = n + k - 1
        terms = min(n - 1, k)

        numerator = 1
        denominator = 1
        for value in range(1, terms + 1):
            numerator = numerator * (total - terms + value) % mod
            denominator = denominator * value % mod

        return numerator * pow(denominator, mod - 2, mod) % mod
