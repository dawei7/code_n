def solve(nums: list[int]) -> int:
    answer = 0
    for left, x in enumerate(nums):
        for y in nums[left:]:
            if abs(x - y) <= min(x, y):
                answer = max(answer, x ^ y)
    return answer
