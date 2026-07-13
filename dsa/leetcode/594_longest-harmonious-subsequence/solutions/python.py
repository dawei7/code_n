from collections import Counter


def solve(nums: list[int]) -> int:
    """Return the largest total frequency of adjacent values."""
    counts = Counter(nums)
    longest = 0

    for value, frequency in counts.items():
        if value + 1 in counts:
            longest = max(longest, frequency + counts[value + 1])

    return longest

