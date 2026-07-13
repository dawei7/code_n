def solve(cost, target):
    costs = list(cost[:9])
    if len(costs) < 9:
        costs.extend([target + 1] * (9 - len(costs)))
    dp = [""] + [None] * target
    for total in range(1, target + 1):
        best = None
        for digit in range(9, 0, -1):
            price = costs[digit - 1]
            if total >= price and dp[total - price] is not None:
                candidate = dp[total - price] + str(digit)
                candidate = "".join(sorted(candidate, reverse=True))
                if best is None or len(candidate) > len(best) or (len(candidate) == len(best) and candidate > best):
                    best = candidate
        dp[total] = best
    return dp[target] or "0"
