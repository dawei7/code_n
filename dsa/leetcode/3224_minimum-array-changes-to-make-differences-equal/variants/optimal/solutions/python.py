def solve(nums: list[int], k: int) -> int:
    savings_delta = [0] * (k + 2)
    pair_count = len(nums) // 2
    for index in range(pair_count):
        left = nums[index]
        right = nums[-index - 1]
        difference = abs(left - right)
        one_change_limit = max(left, right, k - left, k - right)
        savings_delta[0] += 1
        savings_delta[one_change_limit + 1] -= 1
        savings_delta[difference] += 1
        savings_delta[difference + 1] -= 1

    best_savings = current_savings = 0
    for target in range(k + 1):
        current_savings += savings_delta[target]
        best_savings = max(best_savings, current_savings)
    return 2 * pair_count - best_savings
