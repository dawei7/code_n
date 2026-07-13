from collections import deque


def solve(nums: list[int], k: int) -> list[int]:
    candidates: deque[int] = deque()
    answer: list[int] = []
    for index, value in enumerate(nums):
        while candidates and candidates[0] <= index - k:
            candidates.popleft()
        while candidates and nums[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(index)
        if index >= k - 1:
            answer.append(nums[candidates[0]])
    return answer
