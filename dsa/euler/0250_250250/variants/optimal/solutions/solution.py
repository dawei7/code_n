def solve(limit: int = 250250, mod: int = 10**16) -> int:
    """Find the number of non-empty subsets of {1^1, ..., limit^limit} whose sum is divisible by 250.
    
    Time Complexity: O(limit + 250^2)
    Space Complexity: O(250)
    """
    if limit < 1:
        return 0

    counts = [0] * 250
    full_periods = limit // 500
    remainder = limit % 500

    period_counts = [0] * 250
    for i in range(1, 501):
        period_counts[pow(i, i, 250)] += 1

    for r in range(250):
        counts[r] = period_counts[r] * full_periods

    for i in range(1, remainder + 1):
        counts[pow(i, i, 250)] += 1

    dp = [0] * 250
    dp[0] = 1

    for r in range(250):
        cnt = counts[r]
        if not cnt or r == 0:
            if r == 0 and cnt:
                multiplier = pow(2, cnt, mod)
                dp = [(x * multiplier) % mod for x in dp]
            continue

        for _ in range(cnt):
            nxt = list(dp)
            for i in range(250):
                target = (i + r) % 250
                val = nxt[target] + dp[i]
                nxt[target] = val % mod if val >= mod else val
            dp = nxt

    return (dp[0] - 1) % mod

