def solve(nums: list[int]) -> bool:
    n = len(nums) - 1
    if n < 1:
        return False

    counts = [0] * (n + 1)
    for value in nums:
        if value < 1 or value > n:
            return False
        counts[value] += 1

    return counts[n] == 2 and all(
        counts[value] == 1 for value in range(1, n)
    )
