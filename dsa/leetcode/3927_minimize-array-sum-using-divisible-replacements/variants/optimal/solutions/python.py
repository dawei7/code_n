def solve(nums: list[int]) -> int:
    limit = max(nums)
    present = set(nums)
    smallest_divisor = {value: value for value in present}

    for divisor in sorted(present):
        for multiple in range(divisor, limit + 1, divisor):
            if multiple in smallest_divisor and divisor < smallest_divisor[multiple]:
                smallest_divisor[multiple] = divisor

    return sum(smallest_divisor[value] for value in nums)
