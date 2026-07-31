def solve(n: int, restrictions: list[list[int]], diff: list[int]) -> int:
    bounds = [10**30] * n
    bounds[0] = 0
    for index, maximum in restrictions:
        bounds[index] = min(bounds[index], maximum)

    for index in range(1, n):
        bounds[index] = min(bounds[index], bounds[index - 1] + diff[index - 1])
    for index in range(n - 2, -1, -1):
        bounds[index] = min(bounds[index], bounds[index + 1] + diff[index])

    return max(bounds)
