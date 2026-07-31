def solve(nums: list[int], k: int) -> int:
    present = set(nums)
    candidate = k
    while candidate in present:
        candidate += k
    return candidate
