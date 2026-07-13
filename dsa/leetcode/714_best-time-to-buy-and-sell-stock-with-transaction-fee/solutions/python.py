def solve(prices: list[int], fee: int) -> int:
    cash = 0
    hold = -prices[0]

    for price in prices[1:]:
        previous_cash = cash
        cash = max(cash, hold + price - fee)
        hold = max(hold, previous_cash - price)

    return cash
