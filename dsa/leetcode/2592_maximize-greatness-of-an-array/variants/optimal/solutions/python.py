def solve(nums: list[int]) -> int:
    frequencies = {}
    largest_frequency = 0

    for value in nums:
        frequencies[value] = frequencies.get(value, 0) + 1
        largest_frequency = max(largest_frequency, frequencies[value])

    return len(nums) - largest_frequency
