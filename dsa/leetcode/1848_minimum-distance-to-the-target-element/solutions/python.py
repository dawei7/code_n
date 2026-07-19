def solve(nums: list[int], target: int, start: int) -> int:
    """Return the nearest index distance from start to target."""
    return min(
        abs(index - start)
        for index, value in enumerate(nums)
        if value == target
    )
