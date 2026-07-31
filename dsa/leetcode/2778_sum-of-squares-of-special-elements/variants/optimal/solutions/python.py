def solve(nums: list[int]) -> int:
    n = len(nums)
    total = 0
    divisor = 1

    while divisor * divisor <= n:
        if n % divisor == 0:
            total += nums[divisor - 1] ** 2
            paired_divisor = n // divisor
            if paired_divisor != divisor:
                total += nums[paired_divisor - 1] ** 2
        divisor += 1

    return total
