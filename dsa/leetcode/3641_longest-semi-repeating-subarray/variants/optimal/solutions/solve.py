def solve(nums: list[int], k: int) -> int:
    frequencies: dict[int, int] = {}
    repeating_values = 0
    left = 0
    longest = 0

    for right, value in enumerate(nums):
        frequency = frequencies.get(value, 0) + 1
        frequencies[value] = frequency
        if frequency == 2:
            repeating_values += 1

        while repeating_values > k:
            left_value = nums[left]
            if frequencies[left_value] == 2:
                repeating_values -= 1
            frequencies[left_value] -= 1
            left += 1

        longest = max(longest, right - left + 1)

    return longest
