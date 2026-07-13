def solve(costs: list[list[int]]) -> int:
    red = blue = green = 0
    for red_cost, blue_cost, green_cost in costs:
        red, blue, green = (
            red_cost + min(blue, green),
            blue_cost + min(red, green),
            green_cost + min(red, blue),
        )
    return min(red, blue, green)
