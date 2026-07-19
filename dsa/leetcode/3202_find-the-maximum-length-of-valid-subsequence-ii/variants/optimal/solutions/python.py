def solve(nums: list[int], k: int) -> int:
    dp = [[0] * k for _ in range(k)]
    best = 0

    for x in nums:
        r = x % k
        for prev_r in range(k):
            dp[prev_r][r] = dp[r][prev_r] + 1
            if dp[prev_r][r] > best:
                best = dp[prev_r][r]

    return best
