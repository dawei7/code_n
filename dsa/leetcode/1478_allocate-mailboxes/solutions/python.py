def solve(houses, k):
    houses = sorted(houses)
    n = len(houses)
    if n == 0:
        return 0
    k = max(1, min(int(k), n))
    cost = [[0] * n for _ in range(n)]
    for left in range(n):
        for right in range(left, n):
            mid = (left + right) // 2
            cost[left][right] = sum(abs(houses[i] - houses[mid]) for i in range(left, right + 1))
    inf = 10**18
    dp = [[inf] * n for _ in range(k + 1)]
    for i in range(n):
        dp[1][i] = cost[0][i]
    for boxes in range(2, k + 1):
        for i in range(n):
            for prev in range(i):
                dp[boxes][i] = min(dp[boxes][i], dp[boxes - 1][prev] + cost[prev + 1][i])
    return dp[k][n - 1]
