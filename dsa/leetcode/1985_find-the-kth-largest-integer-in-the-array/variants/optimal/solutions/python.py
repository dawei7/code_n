def solve(nums: list[str], k: int) -> str:
    ordered = sorted(nums, key=lambda value: (len(value), value))
    return ordered[-k]
