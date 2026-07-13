def solve(nums):
    increments = 0
    doubles = 0
    for num in nums:
        value = max(0, num)
        increments += value.bit_count()
        if value:
            doubles = max(doubles, value.bit_length() - 1)
    return increments + doubles
