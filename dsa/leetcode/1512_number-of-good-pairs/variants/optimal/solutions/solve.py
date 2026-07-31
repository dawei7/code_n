def solve(nums):
    frequencies = {}
    pairs = 0
    for value in nums:
        pairs += frequencies.get(value, 0)
        frequencies[value] = frequencies.get(value, 0) + 1
    return pairs
