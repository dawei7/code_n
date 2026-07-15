"""Optimal app-local solution for LeetCode 1005."""


def solve(nums, k):
    frequencies = [0] * 201
    total = 0
    minimum_magnitude = 101

    for value in nums:
        frequencies[value + 100] += 1
        total += value
        minimum_magnitude = min(minimum_magnitude, abs(value))

    for value in range(-100, 0):
        flips = min(frequencies[value + 100], k)
        total -= 2 * value * flips
        k -= flips
        if k == 0:
            return total

    if k % 2 == 1:
        total -= 2 * minimum_magnitude

    return total
