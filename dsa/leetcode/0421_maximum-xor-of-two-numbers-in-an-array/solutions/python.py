"""Optimal app-local solution for LeetCode 421."""


def solve(nums: list[int]) -> int:
    best = 0
    mask = 0

    for bit in range(30, -1, -1):
        mask |= 1 << bit
        prefixes = {number & mask for number in nums}
        candidate = best | (1 << bit)
        if any((candidate ^ prefix) in prefixes for prefix in prefixes):
            best = candidate

    return best
