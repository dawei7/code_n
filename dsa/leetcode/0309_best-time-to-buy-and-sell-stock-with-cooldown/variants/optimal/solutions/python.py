"""Three-state dynamic programming for LeetCode 309."""


def _max_profit(prices: list[int]) -> int:
    hold = float("-inf")
    sold = float("-inf")
    rest = 0
    for price in prices:
        previous_hold = hold
        previous_sold = sold
        previous_rest = rest
        hold = max(previous_hold, previous_rest - price)
        sold = previous_hold + price
        rest = max(previous_rest, previous_sold)
    return int(max(sold, rest))


def solve(prices: list[int]) -> int:
    return _max_profit(prices)
