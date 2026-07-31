"""Reference solution for LeetCode 1389."""


def solve(nums: list[int], index: list[int]) -> list[int]:
    target: list[int] = []
    for value, position in zip(nums, index):
        target.insert(position, value)
    return target
