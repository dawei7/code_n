from bisect import bisect_left

def solve(nums: list[int]) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i, num in enumerate(nums):
        prefix_sum[i + 1] = prefix_sum[i] + num

    dp = [0] * (n + 1)
    best_previous = [0] * (n + 2)

    for i in range(1, n + 1):
        best_previous[i] = max(best_previous[i], best_previous[i - 1])
        previous = best_previous[i]
        dp[i] = dp[previous] + 1

        current_sum = prefix_sum[i] - prefix_sum[previous]
        next_prefix = prefix_sum[i] + current_sum
        next_index = bisect_left(prefix_sum, next_prefix)
        if next_index <= n:
            best_previous[next_index] = max(best_previous[next_index], i)

    return dp[n]
