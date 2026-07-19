def solve(nums: list[int]) -> int:
    plain = nums[0]
    squared = nums[0] * nums[0]
    best = squared

    for value in nums[1:]:
        new_squared = max(
            value * value,
            plain + value * value,
            squared + value,
        )
        new_plain = max(value, plain + value)
        plain, squared = new_plain, new_squared
        best = max(best, squared)

    return best
