def solve(nums: list[int]) -> list[int]:
    n = len(nums)
    observed_sum = 0
    observed_squares = 0
    for value in nums:
        observed_sum += value
        observed_squares += value * value

    expected_sum = n * (n + 1) // 2
    expected_squares = n * (n + 1) * (2 * n + 1) // 6

    difference = observed_sum - expected_sum
    pair_sum = (observed_squares - expected_squares) // difference
    duplicate = (difference + pair_sum) // 2
    missing = duplicate - difference
    return [duplicate, missing]
