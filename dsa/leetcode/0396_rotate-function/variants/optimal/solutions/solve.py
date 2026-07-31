"""Optimal app-local solution for LeetCode 396: Rotate Function."""


def solve(nums: list[int]) -> int:
    length = len(nums)
    total = sum(nums)
    score = sum(index * value for index, value in enumerate(nums))
    best = score

    for rotation in range(1, length):
        score += total - length * nums[length - rotation]
        best = max(best, score)

    return best
