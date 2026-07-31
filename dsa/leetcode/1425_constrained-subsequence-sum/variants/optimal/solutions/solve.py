"""Optimal app-local solution for LeetCode 1425."""

from collections import deque


def solve(nums: list[int], k: int) -> int:
    candidates: deque[tuple[int, int]] = deque()
    answer = nums[0]
    for index, value in enumerate(nums):
        while candidates and candidates[0][0] < index - k:
            candidates.popleft()
        ending_sum = value + max(0, candidates[0][1] if candidates else 0)
        answer = max(answer, ending_sum)
        while candidates and candidates[-1][1] <= ending_sum:
            candidates.pop()
        candidates.append((index, ending_sum))
    return answer
