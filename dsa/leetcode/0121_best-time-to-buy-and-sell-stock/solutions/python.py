def solve(prices: list[int]) -> int:
    best = 0
    lowest = float("inf")
    for price in prices:
        lowest = min(lowest, price)
        best = max(best, price - lowest)
    return best
