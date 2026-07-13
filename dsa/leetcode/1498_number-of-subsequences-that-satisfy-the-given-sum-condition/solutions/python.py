def solve(nums, target):
    mod = 1_000_000_007
    nums = sorted(nums)
    powers = [1] * (len(nums) + 1)
    for i in range(1, len(powers)):
        powers[i] = (powers[i - 1] * 2) % mod
    left, right = 0, len(nums) - 1
    answer = 0
    while left <= right:
        if nums[left] + nums[right] <= target:
            answer = (answer + powers[right - left]) % mod
            left += 1
        else:
            right -= 1
    return answer
