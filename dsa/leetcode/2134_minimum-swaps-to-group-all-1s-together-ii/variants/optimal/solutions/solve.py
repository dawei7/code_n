def solve(nums: list[int]) -> int:
    n = len(nums)
    ones = sum(nums)
    if ones <= 1:
        return 0

    zeros = ones - sum(nums[:ones])
    answer = zeros
    for right in range(ones, ones + n - 1):
        zeros += 1 - nums[right % n]
        zeros -= 1 - nums[(right - ones) % n]
        answer = min(answer, zeros)
    return answer
