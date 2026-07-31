"""Optimal solution for LeetCode 3028: Ant on the Boundary."""


def solve(nums: list[int]) -> int:
    position = 0
    answer = 0

    for movement in nums:
        position += movement
        if position == 0:
            answer += 1

    return answer
