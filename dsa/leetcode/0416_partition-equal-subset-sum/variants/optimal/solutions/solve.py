"""Optimal app-local solution for LeetCode 416."""


def solve(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False

    target = total // 2
    reachable = 1
    for value in nums:
        reachable |= reachable << value

    return bool(reachable & (1 << target))
