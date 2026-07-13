def solve(nums: list[int]) -> int:
    before_previous = 0
    previous = 0
    for amount in nums:
        before_previous, previous = previous, max(previous, before_previous + amount)
    return previous
