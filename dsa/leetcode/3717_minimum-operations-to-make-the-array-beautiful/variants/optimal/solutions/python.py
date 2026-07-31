def solve(nums: list[int]) -> int:
    limit = 2 * max(nums)
    infinity = 10**9

    dp = [infinity] * (limit + 1)
    dp[nums[0]] = 0

    for original in nums[1:]:
        next_dp = [infinity] * (limit + 1)
        for previous in range(1, limit + 1):
            if dp[previous] == infinity:
                continue

            first_multiple = (original + previous - 1) // previous * previous
            for value in range(first_multiple, limit + 1, previous):
                next_dp[value] = min(
                    next_dp[value],
                    dp[previous] + value - original,
                )
        dp = next_dp

    return min(dp)
