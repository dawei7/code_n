def solve(nums: list[int]) -> int:
    increasing_end = 0
    while increasing_end + 1 < len(nums) and nums[increasing_end] < nums[increasing_end + 1]:
        increasing_end += 1

    decreasing_start = len(nums) - 1
    while decreasing_start > 0 and nums[decreasing_start - 1] > nums[decreasing_start]:
        decreasing_start -= 1

    total = sum(nums)
    left_sum = 0
    answer = None
    for split, value in enumerate(nums[:-1]):
        left_sum += value
        if split <= increasing_end and split + 1 >= decreasing_start:
            difference = abs(2 * left_sum - total)
            answer = difference if answer is None else min(answer, difference)

    return -1 if answer is None else answer
