mod = 1000000007

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = k * dp[i - 1][1] % mod
            dp[i][1] = ((k - 1) * dp[i - 1][1] + dp[i - 1][0]) % mod
        ans = dp[n][0] % mod
        if ans < 0:
            ans += mod
        results.append(ans)
    print('\n'.join(map(str, results)))


if __name__ == "__main__":
    solve()
