"""Optimal app-local solution for LeetCode 1438."""

from collections import deque


def solve(nums: list[int], limit: int) -> int:
    min_deque = deque()
    max_deque = deque()
    left = 0
    best = 0

    for right, value in enumerate(nums):
        while min_deque and nums[min_deque[-1]] >= value:
            min_deque.pop()
        while max_deque and nums[max_deque[-1]] <= value:
            max_deque.pop()
        min_deque.append(right)
        max_deque.append(right)

        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            if min_deque[0] == left:
                min_deque.popleft()
            if max_deque[0] == left:
                max_deque.popleft()
            left += 1

        best = max(best, right - left + 1)

    return best
