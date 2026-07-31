def solve(nums: list[int]) -> int:
    latest = {}
    best = len(nums)
    for right, value in enumerate(nums):
        left = latest.get(value)
        if left is not None:
            best = min(best, right - left)
        reversed_value = int(str(value)[::-1])
        latest[reversed_value] = right
    return -1 if best == len(nums) else best
