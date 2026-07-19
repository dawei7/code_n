def solve(nums: list[int]) -> int:
    modulo = 1_000_000_007
    maximum = max(nums)
    frequency = [0] * (maximum + 1)
    for value in nums:
        frequency[value] += 1

    prefix_count = [0] * (maximum + 1)
    for value in range(1, maximum + 1):
        prefix_count[value] = prefix_count[value - 1] + frequency[value]

    answer = 0
    for denominator in range(1, maximum + 1):
        denominator_count = frequency[denominator]
        if denominator_count == 0:
            continue

        for lower in range(denominator, maximum + 1, denominator):
            upper = min(lower + denominator - 1, maximum)
            numerator_count = prefix_count[upper] - prefix_count[lower - 1]
            answer += (
                denominator_count
                * (lower // denominator)
                * numerator_count
            )

    return answer % modulo
