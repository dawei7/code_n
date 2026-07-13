def solve(nums: list[int]) -> int:
    total = sum(nums)
    left = 0
    valid = 0

    for value in nums:
        right = total - left - value
        if value == 0:
            if left == right:
                valid += 2
            elif abs(left - right) == 1:
                valid += 1
        left += value

    return valid
