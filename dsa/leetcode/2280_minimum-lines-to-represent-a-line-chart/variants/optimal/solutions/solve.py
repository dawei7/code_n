def solve(stockPrices: list[list[int]]) -> int:
    if len(stockPrices) == 1:
        return 0

    stockPrices.sort()
    lines = 1

    for index in range(2, len(stockPrices)):
        previous_day_change = stockPrices[index - 1][0] - stockPrices[index - 2][0]
        previous_price_change = stockPrices[index - 1][1] - stockPrices[index - 2][1]
        current_day_change = stockPrices[index][0] - stockPrices[index - 1][0]
        current_price_change = stockPrices[index][1] - stockPrices[index - 1][1]

        if previous_price_change * current_day_change != current_price_change * previous_day_change:
            lines += 1

    return lines
