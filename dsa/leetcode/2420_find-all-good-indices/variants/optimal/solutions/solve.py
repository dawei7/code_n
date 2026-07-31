def solve(nums: list[int], k: int) -> list[int]:
    size = len(nums)
    non_increasing = [1] * size
    non_decreasing = [1] * size

    for index in range(1, size):
        if nums[index - 1] >= nums[index]:
            non_increasing[index] = non_increasing[index - 1] + 1

    for index in range(size - 2, -1, -1):
        if nums[index] <= nums[index + 1]:
            non_decreasing[index] = non_decreasing[index + 1] + 1

    return [index for index in range(k, size - k) if non_increasing[index - 1] >= k and non_decreasing[index + 1] >= k]
