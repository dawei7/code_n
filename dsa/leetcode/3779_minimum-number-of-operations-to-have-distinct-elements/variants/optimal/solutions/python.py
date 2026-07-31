from collections import Counter


def solve(nums: list[int]) -> int:
    frequencies = Counter(nums)
    duplicate_values = sum(count > 1 for count in frequencies.values())
    removed = 0
    operations = 0

    while duplicate_values:
        for _ in range(3):
            if removed == len(nums):
                break
            value = nums[removed]
            if frequencies[value] == 2:
                duplicate_values -= 1
            frequencies[value] -= 1
            removed += 1
        operations += 1

    return operations
