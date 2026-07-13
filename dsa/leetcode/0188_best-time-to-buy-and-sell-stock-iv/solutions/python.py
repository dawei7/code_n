def solve(k: int, prices: list[int]) -> int:
    if k == 0 or len(prices) < 2:
        return 0
    if k >= len(prices) // 2:
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))

    buy = [float("-inf")] * (k + 1)
    sell = [0] * (k + 1)
    for price in prices:
        for transaction in range(1, k + 1):
            buy[transaction] = max(buy[transaction], sell[transaction - 1] - price)
            sell[transaction] = max(sell[transaction], buy[transaction] + price)
    return sell[k]
