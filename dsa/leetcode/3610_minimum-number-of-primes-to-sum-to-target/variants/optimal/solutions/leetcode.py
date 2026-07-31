class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        is_prime = [True] * (n + 1)
        if n >= 0:
            is_prime[0] = False
        if n >= 1:
            is_prime[1] = False

        limit = int(n**0.5)
        for value in range(2, limit + 1):
            if is_prime[value]:
                for multiple in range(value * value, n + 1, value):
                    is_prime[multiple] = False

        primes = []
        for value in range(2, n + 1):
            if is_prime[value]:
                primes.append(value)
                if len(primes) == m:
                    break

        unreachable = n + 1
        dp = [unreachable] * (n + 1)
        dp[0] = 0

        for total in range(1, n + 1):
            for prime in primes:
                if prime > total:
                    break
                dp[total] = min(dp[total], dp[total - prime] + 1)

        return dp[n] if dp[n] != unreachable else -1
