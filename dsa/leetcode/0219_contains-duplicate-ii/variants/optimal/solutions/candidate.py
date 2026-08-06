def solve(nums: list[int], k: int) -> bool:
    seen: set[int] = set()
    for i, x in enumerate(nums):
        if x in seen:
            return True
        seen.add(x)
        if i >= k:
            seen.remove(nums[i - k])
    return False
