def solve(nums: list[int]) -> int:
    total = 0
    count = 0

    for value in nums:
        if value % 6 == 0:
            total += value
            count += 1

    return total // count if count else 0
