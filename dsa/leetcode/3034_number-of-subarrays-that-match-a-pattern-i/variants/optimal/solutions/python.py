"""Optimal solution for LeetCode 3034: Number of Subarrays That Match a Pattern I."""


def solve(nums: list[int], pattern: list[int]) -> int:
    answer = 0

    for start in range(len(nums) - len(pattern)):
        for offset, expected_relation in enumerate(pattern):
            left = nums[start + offset]
            right = nums[start + offset + 1]
            actual_relation = (right > left) - (right < left)
            if actual_relation != expected_relation:
                break
        else:
            answer += 1

    return answer
