from collections import deque


def solve(nums: list[int], k: int) -> list[int]:
    candidates: deque[int] = deque()
    answer: list[int] = []

    for i, x in enumerate(nums):
        while candidates and candidates[0] <= i - k:
            candidates.popleft()
        while candidates and nums[candidates[-1]] <= x:
            candidates.pop()

        candidates.append(i)
        if i >= k - 1:
            answer.append(nums[candidates[0]])

    return answer
