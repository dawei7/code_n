"""Optimal solution for LeetCode 368: Largest Divisible Subset."""


def solve(nums: list[int]) -> list[int]:
    if not nums:
        return []

    values = sorted(nums)
    lengths = [1] * len(values)
    previous = [-1] * len(values)
    best_index = 0

    for current in range(len(values)):
        for earlier in range(current):
            if (
                values[current] % values[earlier] == 0
                and lengths[earlier] + 1 > lengths[current]
            ):
                lengths[current] = lengths[earlier] + 1
                previous[current] = earlier
        if lengths[current] > lengths[best_index]:
            best_index = current

    subset: list[int] = []
    while best_index != -1:
        subset.append(values[best_index])
        best_index = previous[best_index]
    subset.reverse()
    return subset

