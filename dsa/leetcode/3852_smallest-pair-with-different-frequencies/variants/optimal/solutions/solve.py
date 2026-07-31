def solve(nums: list[int]) -> list[int]:
    frequencies = [0] * 101

    for value in nums:
        frequencies[value] += 1

    x = next(value for value in range(1, 101) if frequencies[value] > 0)

    for y in range(x + 1, 101):
        if frequencies[y] > 0 and frequencies[y] != frequencies[x]:
            return [x, y]

    return [-1, -1]
