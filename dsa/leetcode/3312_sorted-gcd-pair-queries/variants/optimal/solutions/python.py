from bisect import bisect_right


def solve(nums: list[int], queries: list[int]) -> list[int]:
    limit = max(nums)
    frequency = [0] * (limit + 1)
    for number in nums:
        frequency[number] += 1

    exact_pairs = [0] * (limit + 1)

    for divisor in range(limit, 0, -1):
        divisible = 0
        for multiple in range(divisor, limit + 1, divisor):
            divisible += frequency[multiple]

        pairs = divisible * (divisible - 1) // 2
        for multiple in range(divisor * 2, limit + 1, divisor):
            pairs -= exact_pairs[multiple]
        exact_pairs[divisor] = pairs

    cumulative = [0] * (limit + 1)
    for divisor in range(1, limit + 1):
        cumulative[divisor] = cumulative[divisor - 1] + exact_pairs[divisor]

    return [bisect_right(cumulative, query) for query in queries]
