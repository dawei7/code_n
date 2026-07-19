def solve(prices: list[int]) -> int:
    return sum(max(0, prices[index] - prices[index - 1]) for index in range(1, len(prices)))
