def solve(nums: list[int]) -> int:
    plus = 0
    minus = 0

    for value in nums:
        previous_plus = plus
        previous_minus = minus
        plus = max(previous_plus, previous_minus + value)
        minus = max(previous_minus, previous_plus - value)

    return plus
