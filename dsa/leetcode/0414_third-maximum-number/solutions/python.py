"""Optimal app-local solution for LeetCode 414: Third Maximum Number."""


def solve(nums: list[int]) -> int:
    first: int | None = None
    second: int | None = None
    third: int | None = None

    for value in nums:
        if value == first or value == second or value == third:
            continue
        if first is None or value > first:
            first, second, third = value, first, second
        elif second is None or value > second:
            second, third = value, second
        elif third is None or value > third:
            third = value

    return first if third is None else third
