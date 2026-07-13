"""Optimal app-local solution for LeetCode 410: Split Array Largest Sum."""


def solve(nums: list[int], m: int) -> int:
    lower = max(nums)
    upper = sum(nums)

    while lower < upper:
        limit = (lower + upper) // 2
        groups = 1
        current = 0

        for value in nums:
            if current + value > limit:
                groups += 1
                current = value
            else:
                current += value

        if groups <= m:
            upper = limit
        else:
            lower = limit + 1

    return lower
