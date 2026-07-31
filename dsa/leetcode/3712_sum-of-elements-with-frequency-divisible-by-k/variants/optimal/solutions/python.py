def solve(nums: list[int], k: int) -> int:
    frequencies = [0] * 101
    for value in nums:
        frequencies[value] += 1

    total = 0
    for value, frequency in enumerate(frequencies):
        if frequency > 0 and frequency % k == 0:
            total += value * frequency
    return total
