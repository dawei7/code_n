from collections import deque


def solve(nums):
    maximums = deque()
    minimums = deque()
    left = 0
    total = 0

    for right, value in enumerate(nums):
        while maximums and nums[maximums[-1]] <= value:
            maximums.pop()
        while minimums and nums[minimums[-1]] >= value:
            minimums.pop()

        maximums.append(right)
        minimums.append(right)

        while nums[maximums[0]] - nums[minimums[0]] > 2:
            if maximums[0] == left:
                maximums.popleft()
            if minimums[0] == left:
                minimums.popleft()
            left += 1

        total += right - left + 1

    return total
