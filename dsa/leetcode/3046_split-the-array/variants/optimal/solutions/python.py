def solve(nums: list[int]) -> bool:
    counts = [0] * 101

    for value in nums:
        counts[value] += 1
        if counts[value] > 2:
            return False

    return True
