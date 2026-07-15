"""Optimal app-local solution for LeetCode 1121."""


def solve(nums, k):
    maximum_frequency = current_frequency = 1
    for index in range(1, len(nums)):
        if nums[index] == nums[index - 1]:
            current_frequency += 1
        else:
            maximum_frequency = max(maximum_frequency, current_frequency)
            current_frequency = 1
    maximum_frequency = max(maximum_frequency, current_frequency)
    return len(nums) >= maximum_frequency * k
