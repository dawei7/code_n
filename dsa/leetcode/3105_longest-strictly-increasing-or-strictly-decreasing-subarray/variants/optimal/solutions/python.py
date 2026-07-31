def solve(nums: list[int]) -> int:
    increasing = decreasing = answer = 1

    for index in range(1, len(nums)):
        if nums[index] > nums[index - 1]:
            increasing += 1
            decreasing = 1
        elif nums[index] < nums[index - 1]:
            decreasing += 1
            increasing = 1
        else:
            increasing = decreasing = 1

        answer = max(answer, increasing, decreasing)

    return answer
