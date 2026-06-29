def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        dp = [10 ** 9] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if i + 1 <= n:
                dp[i + 1] = min(dp[i + 1], dp[i] + 1)
            if i > 0 and 2 * i <= n and (s[:i] == s[i:2 * i]):
                dp[2 * i] = min(dp[2 * i], dp[i] + 1)
        results.append(str(dp[n]))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
