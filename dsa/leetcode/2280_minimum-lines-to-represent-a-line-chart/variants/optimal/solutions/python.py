def solve(stockPrices: list[list[int]]) -> int:
    if len(stockPrices) == 1:
        return 0

    points = sorted(stockPrices)
    lines = 1

    for index in range(2, len(points)):
        previous_dx = points[index - 1][0] - points[index - 2][0]
        previous_dy = points[index - 1][1] - points[index - 2][1]
        current_dx = points[index][0] - points[index - 1][0]
        current_dy = points[index][1] - points[index - 1][1]

        if previous_dy * current_dx != current_dy * previous_dx:
            lines += 1

    return lines
