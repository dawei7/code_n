def solve(nums: list[int]) -> int:
    first_index: dict[int, int] = {}
    counts: dict[int, int] = {}
    degree = 0
    shortest = len(nums)

    for index, value in enumerate(nums):
        if value not in first_index:
            first_index[value] = index
        counts[value] = counts.get(value, 0) + 1
        span = index - first_index[value] + 1

        if counts[value] > degree:
            degree = counts[value]
            shortest = span
        elif counts[value] == degree:
            shortest = min(shortest, span)

    return shortest
