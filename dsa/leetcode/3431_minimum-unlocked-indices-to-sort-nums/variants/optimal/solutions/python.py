def solve(nums: list[int], locked: list[int]) -> int:
    n = len(nums)
    first_two = n
    first_three = n
    last_one = -1
    last_two = -1

    for i, value in enumerate(nums):
        if value == 1:
            last_one = i
        elif value == 2:
            first_two = min(first_two, i)
            last_two = i
        else:
            first_three = min(first_three, i)

    if first_three < last_one:
        return -1

    return sum(
        locked[i]
        for i in range(n)
        if first_two <= i < last_one or first_three <= i < last_two
    )
