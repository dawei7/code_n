def solve(x: list[int], y: list[int]) -> int:
    best_for_x: dict[int, int] = {}
    for x_value, y_value in zip(x, y, strict=True):
        best_for_x[x_value] = max(best_for_x.get(x_value, 0), y_value)

    if len(best_for_x) < 3:
        return -1

    first = second = third = 0
    for value in best_for_x.values():
        if value > first:
            first, second, third = value, first, second
        elif value > second:
            second, third = value, second
        elif value > third:
            third = value

    return first + second + third
