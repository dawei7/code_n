


def solve():
    t = int(input())

    def max(a, b):
        return a if a > b else b

    for _ in range(t):
        n = int(input())
        dp = [0] * (n + 1)
        C = list(map(int,input().split()))
        dp[1] = max(0, C[0])
        dp[2] = max(dp[1], C[1])
        for i in range(3, n + 1):
            dp[i] = max(dp[i - 2] + C[i-1], dp[i - 1])
        ans = 0

        for i in range(1, n + 1):
            ans = max(ans, dp[i])

        print(ans)


if __name__ == "__main__":
    solve()
