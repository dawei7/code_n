def solve(nums: list[int]) -> int:
    answer = 0
    for value in nums:
        answer ^= value
    return answer
