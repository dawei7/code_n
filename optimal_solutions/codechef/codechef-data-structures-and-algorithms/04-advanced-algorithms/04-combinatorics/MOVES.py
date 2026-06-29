


def solve():
    MOD = 10**9 + 7
    N = 5001

    class Solution:
        def __init__(self):
            # Precompute factorials and inverse factorials once
            self.fact = [1] * N
            self.invFact = [1] * N
            for i in range(1, N):
                self.fact[i] = (self.fact[i - 1] * i) % MOD
            self.invFact[N - 1] = pow(self.fact[N - 1], MOD - 2, MOD)
            for i in range(N - 2, -1, -1):
                self.invFact[i] = (self.invFact[i + 1] * (i + 1)) % MOD

        def nCr(self, n, k):
            if k < 0 or k > n:
                return 0
            return (self.fact[n] * self.invFact[k] % MOD * self.invFact[n - k]) % MOD

        def compute(self, n, k):
            if n < 2:
                return 0
            part1 = self.nCr(n - 2, k // 2)
            part2 = self.nCr(n - 2, (k - 1) // 2)
            return (2 * part1 % MOD * part2) % MOD


if __name__ == "__main__":
    solve()
