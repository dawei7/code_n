def solve(digitSum: list[int]) -> int:
    modulo = 1_000_000_007
    limit = 5000

    value_digit_sum = [0] * (limit + 1)
    for value in range(1, limit + 1):
        value_digit_sum[value] = value_digit_sum[value // 10] + value % 10

    ways = [0] * (limit + 1)
    first_sum = digitSum[0]
    for value in range(limit + 1):
        if value_digit_sum[value] == first_sum:
            ways[value] = 1

    for required_sum in digitSum[1:]:
        next_ways = [0] * (limit + 1)
        prefix = 0

        for value in range(limit + 1):
            prefix += ways[value]
            if prefix >= modulo:
                prefix -= modulo

            if value_digit_sum[value] == required_sum:
                next_ways[value] = prefix

        ways = next_ways

    return sum(ways) % modulo
