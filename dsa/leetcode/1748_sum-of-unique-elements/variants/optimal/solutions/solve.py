def solve(nums: list[int]) -> int:
    frequency = [0] * 101
    for value in nums:
        frequency[value] += 1

    return sum(value for value in range(1, 101) if frequency[value] == 1)
