def solve(nums: list[int]) -> int:
    minimum = nums[0]
    answer = -1

    for value in nums[1:]:
        if value > minimum:
            answer = max(answer, value - minimum)
        minimum = min(minimum, value)

    return answer
