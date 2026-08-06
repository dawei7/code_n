def solve(nums: list[int]) -> list[int]:
    answer = [1] * len(nums)
    prefix = 1

    for i, x in enumerate(nums):
        answer[i] = prefix
        prefix *= x

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
