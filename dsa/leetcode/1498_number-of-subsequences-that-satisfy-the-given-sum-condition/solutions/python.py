"""Optimal app-local solution for LeetCode 1498."""

MODULUS = 1_000_000_007


def solve(nums: list[int], target: int) -> int:
    """Count valid non-empty subsequences modulo 1_000_000_007."""
    values = sorted(nums)
    powers = [1] * (len(values) + 1)
    for exponent in range(1, len(powers)):
        powers[exponent] = (powers[exponent - 1] * 2) % MODULUS

    left = 0
    right = len(values) - 1
    answer = 0

    while left <= right:
        if values[left] + values[right] <= target:
            answer = (answer + powers[right - left]) % MODULUS
            left += 1
        else:
            right -= 1

    return answer
