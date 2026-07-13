"""Duplicate-aware backtracking for LeetCode 491."""


def solve(nums: list[int]) -> list[list[int]]:
    answer: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        if len(path) >= 2:
            answer.append(path.copy())

        used: set[int] = set()
        for index in range(start, len(nums)):
            value = nums[index]
            if value in used or (path and value < path[-1]):
                continue
            used.add(value)
            path.append(value)
            backtrack(index + 1)
            path.pop()

    backtrack(0)
    return answer
