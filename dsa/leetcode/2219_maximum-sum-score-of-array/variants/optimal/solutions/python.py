def solve(nums: list[int]) -> int:
    left = 0
    right = sum(nums)
    answer = -10**30
    for value in nums:
        left += value
        answer = max(answer, left, right)
        right -= value
    return answer
