"""Optimal app-local solution for LeetCode 446."""


def solve(nums: list[int]) -> int:
    endings: list[dict[int, int]] = [{} for _ in nums]
    answer = 0

    for right in range(len(nums)):
        for left in range(right):
            difference = nums[right] - nums[left]
            extensions = endings[left].get(difference, 0)
            answer += extensions
            endings[right][difference] = endings[right].get(difference, 0) + extensions + 1
    return answer
