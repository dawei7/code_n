def solve(nums: list[int]) -> int:
    answer = 0
    increasing_suffix = 0

    for index, value in enumerate(nums):
        if index == 0 or nums[index - 1] < value:
            increasing_suffix += 1
        else:
            increasing_suffix = 1
        answer += increasing_suffix

    return answer
