"""Optimal app-local solution for LeetCode 1431."""


def solve(candies: list[int], extra_candies: int) -> list[bool]:
    greatest = max(candies)
    return [candy + extra_candies >= greatest for candy in candies]
