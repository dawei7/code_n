def solve(stone_value):
    n = len(stone_value)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        take = 0
        dp[i] = float("-inf")
        for j in range(i, min(i + 3, n)):
            take += stone_value[j]
            dp[i] = max(dp[i], take - dp[j + 1])
    if dp[0] > 0:
        return "Alice"
    if dp[0] < 0:
        return "Bob"
    return "Tie"
