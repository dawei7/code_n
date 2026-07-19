def solve(nums: list[int], k: int) -> int:
    ordered = sorted(nums)
    return min(
        ordered[index + k - 1] - ordered[index]
        for index in range(len(ordered) - k + 1)
    )
