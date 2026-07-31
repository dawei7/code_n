def solve(cost: list[int], time: list[int]) -> int:
    n = len(cost)
    dp = [float("inf")] * (n + 1)
    dp[0] = 0

    for price, duration in zip(cost, time):
        for covered in range(n, -1, -1):
            next_covered = min(n, covered + duration + 1)
            dp[next_covered] = min(dp[next_covered], dp[covered] + price)

    return dp[n]
