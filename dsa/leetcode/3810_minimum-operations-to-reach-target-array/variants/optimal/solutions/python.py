def solve(nums: list[int], target: list[int]) -> int:
    return len(
        {
            current
            for current, desired in zip(nums, target)
            if current != desired
        }
    )
