def solve(nums: list[int]) -> int:
    n = len(nums)
    left = [1] * n
    for index in range(1, n):
        if nums[index - 1] <= nums[index]:
            left[index] = left[index - 1] + 1

    answer = max(left)
    next_run = 0
    for index in range(n - 1, -1, -1):
        if index > 0:
            answer = max(answer, left[index - 1] + 1)
        if index + 1 < n:
            answer = max(answer, next_run + 1)
        if 0 < index < n - 1 and nums[index - 1] <= nums[index + 1]:
            answer = max(answer, left[index - 1] + 1 + next_run)

        if index + 1 < n and nums[index] <= nums[index + 1]:
            next_run += 1
        else:
            next_run = 1

    return min(answer, n)
