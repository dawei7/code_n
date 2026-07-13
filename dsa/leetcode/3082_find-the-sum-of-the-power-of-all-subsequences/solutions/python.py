def solve(nums: list[int], k: int) -> int:
    mod = 10**9 + 7
    dp = [0] * (k + 1)
    dp[0] = 1

    for value in nums:
        nxt = [(count * 2) % mod for count in dp]
        if value <= k:
            for total in range(value, k + 1):
                nxt[total] = (nxt[total] + dp[total - value]) % mod
        dp = nxt

    return dp[k]
