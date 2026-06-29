def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    T = int(data[0])
    results = []
    idx = 1
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        a = []
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            row = list(map(int, data[idx].split()))
            a.append(row)
            for j in range(n):
                dp[i][j] = 0
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                elif i > 0:
                    dp[i][j] = dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = dp[i][j - 1]
                dp[i][j] += a[i][j]
            idx += 1
        if dp[n - 1][n - 1] < 0:
            results.append('Bad Judges')
        else:
            results.append(f'{dp[n - 1][n - 1] / (2 * n - 3):.8f}')
    print('\n'.join(results))


if __name__ == "__main__":
    solve()
