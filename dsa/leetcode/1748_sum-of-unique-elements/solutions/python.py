def solve(nums: list[int]) -> int:
    frequency = [0] * 101
    unique_sum = 0

    for value in nums:
        if frequency[value] == 0:
            unique_sum += value
        elif frequency[value] == 1:
            unique_sum -= value
        frequency[value] += 1

    return unique_sum
