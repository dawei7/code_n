def solve(houses, cost, m, n, target):
    houses = list(houses)
    m = min(len(houses), int(m)) if isinstance(m, int) and m > 0 else len(houses)
    houses = houses[:m]
    colors = max(1, int(n) if isinstance(n, int) and n > 0 else max((len(row) for row in cost if isinstance(row, list)), default=1))
    target = max(1, min(int(target), m)) if m else 0
    prices = []
    for i in range(m):
        row = cost[i] if i < len(cost) and isinstance(cost[i], list) else []
        padded = [abs(int(row[j])) if j < len(row) else 10**6 for j in range(colors)]
        prices.append(padded)
    inf = 10**18
    dp = {(0, 0): 0}
    for i, painted in enumerate(houses):
        next_dp = {}
        available = [painted] if isinstance(painted, int) and 1 <= painted <= colors else range(1, colors + 1)
        for color in available:
            paint_cost = 0 if painted == color else prices[i][color - 1]
            for (prev, groups), value in dp.items():
                new_groups = groups + (color != prev)
                if new_groups <= target:
                    key = (color, new_groups)
                    candidate = value + paint_cost
                    if candidate < next_dp.get(key, inf):
                        next_dp[key] = candidate
        dp = next_dp
    answer = min((value for (color, groups), value in dp.items() if groups == target), default=inf)
    return -1 if answer == inf else answer
