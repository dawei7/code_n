def solve(arr, difference):
    dp = {}
    best = 0
    for value in arr:
        dp[value] = dp.get(value - difference, 0) + 1
        best = max(best, dp[value])
    return best
