from collections import deque


def solve(nums, k):
    if not nums:
        return 0
    k = max(1, int(k))
    best = nums[:]
    queue = deque()
    answer = nums[0]
    for index, value in enumerate(nums):
        while queue and queue[0] < index - k:
            queue.popleft()
        if queue:
            best[index] = value + max(0, best[queue[0]])
        answer = max(answer, best[index])
        while queue and best[queue[-1]] <= best[index]:
            queue.pop()
        queue.append(index)
    return answer
