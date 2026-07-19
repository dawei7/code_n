"""Optimal app-local solution for LeetCode 995."""


def solve(nums, k):
    active_parity = 0
    flips = 0

    for index in range(len(nums)):
        if index >= k and nums[index - k] == 2:
            active_parity ^= 1

        if nums[index] == active_parity:
            if index + k > len(nums):
                return -1
            nums[index] = 2
            active_parity ^= 1
            flips += 1

    return flips
