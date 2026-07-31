def solve(original: list[int], bounds: list[list[int]]) -> int:
    lower, upper = bounds[0]
    base = original[0]
    for index in range(1, len(original)):
        offset = original[index] - base
        lower = max(lower, bounds[index][0] - offset)
        upper = min(upper, bounds[index][1] - offset)
    return max(0, upper - lower + 1)
