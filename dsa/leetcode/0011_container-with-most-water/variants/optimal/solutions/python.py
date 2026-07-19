"""Optimal solution for LeetCode 11: Container With Most Water."""


def solve(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    best = 0
    while left < right:
        width = right - left
        best = max(best, width * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
