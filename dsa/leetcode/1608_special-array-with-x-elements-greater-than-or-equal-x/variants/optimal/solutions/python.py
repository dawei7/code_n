def solve(nums: list[int]) -> int:
    ordered = sorted(nums)
    length = len(ordered)
    for index, value in enumerate(ordered):
        candidate = length - index
        if value >= candidate and (index == 0 or ordered[index - 1] < candidate):
            return candidate
    return -1
