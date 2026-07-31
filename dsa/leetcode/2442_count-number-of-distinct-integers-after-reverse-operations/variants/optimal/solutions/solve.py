def solve(nums: list[int]) -> int:
    values = set(nums)

    for value in nums:
        reversed_value = 0
        while value:
            reversed_value = reversed_value * 10 + value % 10
            value //= 10
        values.add(reversed_value)

    return len(values)
