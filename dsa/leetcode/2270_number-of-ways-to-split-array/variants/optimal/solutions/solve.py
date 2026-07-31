def solve(nums: list[int]) -> int:
    total = sum(nums)
    left = 0
    answer = 0
    for value in nums[:-1]:
        left += value
        if left >= total - left:
            answer += 1
    return answer
