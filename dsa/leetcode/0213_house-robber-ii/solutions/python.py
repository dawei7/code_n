def solve(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def rob_range(start: int, stop: int) -> int:
        before_previous = previous = 0
        for index in range(start, stop):
            before_previous, previous = previous, max(previous, before_previous + nums[index])
        return previous

    return max(rob_range(0, len(nums) - 1), rob_range(1, len(nums)))
