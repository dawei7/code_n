def solve(nums: list[int], k: int) -> list[int]:
    result = []
    consecutive_length = 0

    for index, value in enumerate(nums):
        if index > 0 and value == nums[index - 1] + 1:
            consecutive_length += 1
        else:
            consecutive_length = 1

        if index >= k - 1:
            result.append(value if consecutive_length >= k else -1)

    return result
