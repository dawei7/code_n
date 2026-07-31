def solve(nums: list[int]) -> int:
    even_count = 0
    odd_count = 0
    alternating_end_even = 0
    alternating_end_odd = 0

    for value in nums:
        if value % 2 == 0:
            even_count += 1
            alternating_end_even = alternating_end_odd + 1
        else:
            odd_count += 1
            alternating_end_odd = alternating_end_even + 1

    return max(
        even_count,
        odd_count,
        alternating_end_even,
        alternating_end_odd,
    )
