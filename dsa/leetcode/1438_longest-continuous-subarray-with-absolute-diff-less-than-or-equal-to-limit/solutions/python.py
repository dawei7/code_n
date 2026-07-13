from collections import deque


def solve(nums, limit):
    min_q = deque()
    max_q = deque()
    left = 0
    best = 0
    for right, value in enumerate(nums):
        while min_q and nums[min_q[-1]] >= value:
            min_q.pop()
        while max_q and nums[max_q[-1]] <= value:
            max_q.pop()
        min_q.append(right)
        max_q.append(right)
        while nums[max_q[0]] - nums[min_q[0]] > limit:
            if min_q[0] == left:
                min_q.popleft()
            if max_q[0] == left:
                max_q.popleft()
            left += 1
        best = max(best, right - left + 1)
    return best
