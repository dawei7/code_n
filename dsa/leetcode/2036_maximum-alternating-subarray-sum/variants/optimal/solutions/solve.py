def solve(nums: list[int]) -> int:
    add = nums[0]
    subtract = float("-inf")
    answer = add

    for value in nums[1:]:
        next_add = max(value, subtract + value)
        next_subtract = add - value
        add, subtract = next_add, next_subtract
        answer = max(answer, add, subtract)

    return int(answer)
