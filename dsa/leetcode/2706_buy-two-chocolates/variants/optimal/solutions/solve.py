def solve(prices: list[int], money: int) -> int:
    cheapest = 101
    second_cheapest = 101

    for price in prices:
        if price < cheapest:
            second_cheapest = cheapest
            cheapest = price
        elif price < second_cheapest:
            second_cheapest = price

    cost = cheapest + second_cheapest
    return money - cost if cost <= money else money
