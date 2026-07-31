def solve(nums: list[int], queries: list[list[int]]) -> int:
    modulus = 1_000_000_007

    for left, right, step, multiplier in queries:
        for index in range(left, right + 1, step):
            nums[index] = nums[index] * multiplier % modulus

    answer = 0
    for value in nums:
        answer ^= value
    return answer
