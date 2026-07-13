def solve(n, cuts):
    valid = sorted({cut for cut in cuts if 0 < cut < n})
    points = [0] + valid + [n]
    m = len(points)
    dp = [[0] * m for _ in range(m)]
    for length in range(2, m):
        for left in range(m - length):
            right = left + length
            best = None
            for mid in range(left + 1, right):
                cost = dp[left][mid] + dp[mid][right] + points[right] - points[left]
                if best is None or cost < best:
                    best = cost
            dp[left][right] = 0 if best is None else best
    return dp[0][m - 1]
