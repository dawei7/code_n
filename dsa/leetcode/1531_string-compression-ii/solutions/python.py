def solve(s, k):
    n = len(s)
    infinity = n + 1
    dp = [[infinity] * (k + 1) for _ in range(n + 1)]
    for deletions in range(k + 1):
        dp[n][deletions] = 0

    for start in range(n - 1, -1, -1):
        for deletions in range(k + 1):
            if deletions > 0:
                dp[start][deletions] = dp[start + 1][deletions - 1]
            kept = 0
            removed = 0
            for end in range(start, n):
                if s[end] == s[start]:
                    kept += 1
                else:
                    removed += 1
                if removed > deletions:
                    break
                encoded = 1 if kept == 1 else 2 if kept < 10 else 3 if kept < 100 else 4
                dp[start][deletions] = min(
                    dp[start][deletions], encoded + dp[end + 1][deletions - removed]
                )
    return dp[0][k]
