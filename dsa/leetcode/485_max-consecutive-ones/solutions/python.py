"""Single-pass run-length scan for LeetCode 485."""


def solve(nums: list[int]) -> int:
    best = 0
    current = 0
    for value in nums:
        if value == 1:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best
