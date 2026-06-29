


def solve():
    class Solution:
        MOD = 10**9 + 7
        MAXN = 500

        def __init__(self):
            # Precompute factorials and inverse factorials
            self.fact = [1] * (self.MAXN + 1)
            self.invFact = [1] * (self.MAXN + 1)

            for i in range(1, self.MAXN + 1):
                self.fact[i] = (self.fact[i - 1] * i) % self.MOD

            # Fermat's Little Theorem for inverse factorial
            self.invFact[self.MAXN] = pow(self.fact[self.MAXN], self.MOD - 2, self.MOD)
            for i in range(self.MAXN - 1, -1, -1):
                self.invFact[i] = (self.invFact[i + 1] * (i + 1)) % self.MOD

        def countSmeagoleseAnagrams(self, S: str) -> int:
            from collections import Counter

            freq = Counter(S)
            n = len(S)

            result = self.fact[n]
            for count in freq.values():
                result = (result * self.invFact[count]) % self.MOD

            return result


if __name__ == "__main__":
    solve()
