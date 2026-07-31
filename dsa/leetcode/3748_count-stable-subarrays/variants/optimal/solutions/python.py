def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    n = len(nums)
    stable_ending_prefix = [0] * (n + 1)
    current_start = 0
    for index, value in enumerate(nums):
        if index and nums[index - 1] > value:
            current_start = index
        stable_ending_prefix[index + 1] = (
            stable_ending_prefix[index] + index - current_start + 1
        )

    current_end = n - 1
    nondecreasing_end = [0] * n
    for index in range(n - 1, -1, -1):
        if index == n - 1 or nums[index] > nums[index + 1]:
            current_end = index
        nondecreasing_end[index] = current_end

    result = []
    for left, right in queries:
        first_end = min(right, nondecreasing_end[left])
        length = first_end - left + 1
        result.append(
            length * (length + 1) // 2
            + stable_ending_prefix[right + 1]
            - stable_ending_prefix[first_end + 1]
        )
    return result
