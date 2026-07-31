def solve(nums: list[int]) -> int:
    n = len(nums)

    left = [1] * n
    left[1] = 2
    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            left[i] = left[i - 1] + 1
        else:
            left[i] = 2

    right = [1] * n
    right[n - 2] = 2
    for i in range(n - 3, -1, -1):
        if nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]:
            right[i] = right[i + 1] + 1
        else:
            right[i] = 2

    answer = max(left)

    for i in range(n):
        if i > 0:
            answer = max(answer, left[i - 1] + 1)
        if i + 1 < n:
            answer = max(answer, right[i + 1] + 1)

        if i == 0 or i + 1 == n:
            continue

        gap = nums[i + 1] - nums[i - 1]
        if gap % 2:
            continue

        difference = gap // 2
        left_length = 1
        if i >= 2 and nums[i - 1] - nums[i - 2] == difference:
            left_length = left[i - 1]

        right_length = 1
        if i + 2 < n and nums[i + 2] - nums[i + 1] == difference:
            right_length = right[i + 1]

        answer = max(answer, left_length + 1 + right_length)

    return min(n, answer)
