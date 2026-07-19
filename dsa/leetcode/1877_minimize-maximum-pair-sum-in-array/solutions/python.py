def solve(nums: list[int]) -> int:
    ordered = sorted(nums)
    return max(
        ordered[index] + ordered[-index - 1]
        for index in range(len(ordered) // 2)
    )
