def solve(nums: list[int], k: int) -> list[int]:
    return sorted(set(nums), reverse=True)[:k]
