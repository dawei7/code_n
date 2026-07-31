def solve(x: list[int], y: list[int]) -> int:
    best_for_x: dict[int, int] = {}
    for xi, yi in zip(x, y):
        best_for_x[xi] = max(best_for_x.get(xi, 0), yi)

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
