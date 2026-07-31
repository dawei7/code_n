def solve(cost: list[int]) -> int:
    ordered = sorted(cost, reverse=True)
    return sum(price for index, price in enumerate(ordered) if index % 3 != 2)
