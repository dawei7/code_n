def solve(
    price: list[int],
    tastiness: list[int],
    maxAmount: int,
    maxCoupons: int,
) -> int:
    best = [[0] * (maxAmount + 1) for _ in range(maxCoupons + 1)]

    for cost, value in zip(price, tastiness):
        discounted = cost // 2
        for coupons in range(maxCoupons, -1, -1):
            row = best[coupons]
            previous = best[coupons - 1] if coupons else None
            for budget in range(maxAmount, -1, -1):
                if budget >= cost:
                    row[budget] = max(row[budget], row[budget - cost] + value)
                if previous is not None and budget >= discounted:
                    row[budget] = max(
                        row[budget],
                        previous[budget - discounted] + value,
                    )

    return best[maxCoupons][maxAmount]
