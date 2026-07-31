def solve(nums: list[int]) -> int:
    total = sum(nums)
    suffix_sum = nums[-1]
    suffix_minimum = nums[-1]
    answer = -10**30
    for index in range(len(nums) - 2, -1, -1):
        prefix_sum = total - suffix_sum
        answer = max(answer, prefix_sum - suffix_minimum)
        suffix_sum += nums[index]
        suffix_minimum = min(suffix_minimum, nums[index])
    return answer
