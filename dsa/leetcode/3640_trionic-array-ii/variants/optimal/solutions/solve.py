def solve(nums: list[int]) -> int:
    negative_infinity = float("-inf")
    increasing = negative_infinity
    decreasing = negative_infinity
    trionic = negative_infinity
    answer = negative_infinity

    for index in range(1, len(nums)):
        previous = nums[index - 1]
        current = nums[index]

        if current > previous:
            next_increasing = max(previous + current, increasing + current)
            next_trionic = max(decreasing + current, trionic + current)
            next_decreasing = negative_infinity
        elif current < previous:
            next_increasing = negative_infinity
            next_decreasing = max(increasing + current, decreasing + current)
            next_trionic = negative_infinity
        else:
            next_increasing = negative_infinity
            next_decreasing = negative_infinity
            next_trionic = negative_infinity

        increasing = next_increasing
        decreasing = next_decreasing
        trionic = next_trionic
        answer = max(answer, trionic)

    return int(answer)
