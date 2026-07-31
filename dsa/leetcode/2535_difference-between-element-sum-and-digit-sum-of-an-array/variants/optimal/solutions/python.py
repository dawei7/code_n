def solve(nums: list[int]) -> int:
    element_sum = sum(nums)
    digit_sum = 0

    for value in nums:
        while value:
            digit_sum += value % 10
            value //= 10

    return abs(element_sum - digit_sum)
