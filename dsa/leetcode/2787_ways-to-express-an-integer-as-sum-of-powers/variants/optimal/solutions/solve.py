def solve(n: int, x: int) -> int:
    mod = 1_000_000_007
    dp = [0] * (n + 1)
    dp[0] = 1

    base = 1
    while base**x <= n:
        power = base**x
        for total in range(n, power - 1, -1):
            dp[total] = (dp[total] + dp[total - power]) % mod
        base += 1

    return dp[n]
