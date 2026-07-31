def solve(nums: list[int]) -> int:
    n = len(nums)
    left = [1] * n
    right = [1] * n

    for index in range(1, n):
        if nums[index - 1] <= nums[index]:
            left[index] = left[index - 1] + 1

    for index in range(n - 2, -1, -1):
        if nums[index] <= nums[index + 1]:
            right[index] = right[index + 1] + 1

    answer = max(left)
    for index in range(n):
        if index > 0:
            answer = max(answer, left[index - 1] + 1)
        if index + 1 < n:
            answer = max(answer, right[index + 1] + 1)
        if 0 < index < n - 1 and nums[index - 1] <= nums[index + 1]:
            answer = max(answer, left[index - 1] + 1 + right[index + 1])

    return min(answer, n)
