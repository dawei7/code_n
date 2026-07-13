"""Optimal solution for LeetCode 1389: Create Target Array in the Given Order."""


def solve(nums: list[int], index: list[int]) -> list[int]:
    target: list[int] = []
    for value, pos in zip(nums, index):
        target.insert(pos, value)
    return target
