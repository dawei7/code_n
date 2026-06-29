import sys


def solve():
    MOD = 10**9 + 7

    def calculateRSA(X):
        n = len(X)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            # Single digit decode is valid if digit is not '0'
            if X[i-1] != '0':
                dp[i] = (dp[i] + dp[i-1]) % MOD
            # Check for two-digit decode possibility
            if i >= 2 and X[i-2] != '0':
                two_digit = int(X[i-2:i])
                if 10 <= two_digit <= 26:
                    dp[i] = (dp[i] + dp[i-2]) % MOD
        return dp[n]

    if __name__ == "__main__":
        data = sys.stdin.read().splitlines()
        t = int(data[0])
        results = []
        for i in range(1, t+1):
            results.append(str(calculateRSA(data[i].strip())))
        sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    solve()
