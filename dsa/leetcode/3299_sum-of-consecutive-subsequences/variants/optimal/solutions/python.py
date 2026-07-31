def solve(nums: list[int]) -> int:
    modulus = 1_000_000_007
    limit = max(nums) + 2
    increasing_count = [0] * limit
    increasing_sum = [0] * limit
    decreasing_count = [0] * limit
    decreasing_sum = [0] * limit
    answer = 0

    for value in nums:
        new_increasing_count = (1 + increasing_count[value - 1]) % modulus
        new_increasing_sum = (
            value
            + increasing_sum[value - 1]
            + value * increasing_count[value - 1]
        ) % modulus

        new_decreasing_count = (1 + decreasing_count[value + 1]) % modulus
        new_decreasing_sum = (
            value
            + decreasing_sum[value + 1]
            + value * decreasing_count[value + 1]
        ) % modulus

        answer = (answer + new_increasing_sum + new_decreasing_sum - value) % modulus
        increasing_count[value] = (increasing_count[value] + new_increasing_count) % modulus
        increasing_sum[value] = (increasing_sum[value] + new_increasing_sum) % modulus
        decreasing_count[value] = (decreasing_count[value] + new_decreasing_count) % modulus
        decreasing_sum[value] = (decreasing_sum[value] + new_decreasing_sum) % modulus

    return answer
