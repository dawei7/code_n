def solve(nums: list[int]) -> int:
    frequencies: dict[int, int] = {}
    for value in nums:
        frequencies[value] = frequencies.get(value, 0) + 1

    frequency_counts: dict[int, int] = {}
    for frequency in frequencies.values():
        frequency_counts[frequency] = frequency_counts.get(frequency, 0) + 1

    for value in nums:
        if frequency_counts[frequencies[value]] == 1:
            return value

    return -1
