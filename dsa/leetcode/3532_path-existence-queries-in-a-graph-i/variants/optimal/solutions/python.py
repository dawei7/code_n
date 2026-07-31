def solve(
    n: int,
    nums: list[int],
    maxDiff: int,
    queries: list[list[int]],
) -> list[bool]:
    component = [0] * n

    for index in range(1, n):
        component[index] = component[index - 1]
        if nums[index] - nums[index - 1] > maxDiff:
            component[index] += 1

    return [
        component[source] == component[target]
        for source, target in queries
    ]
