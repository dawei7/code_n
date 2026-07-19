def solve(nums: list[int], left: int, right: int) -> int:
    last_too_large = -1
    last_in_range = -1
    total = 0
    for index, value in enumerate(nums):
        if value > right:
            last_too_large = index
        if left <= value <= right:
            last_in_range = index
        if last_in_range > last_too_large:
            total += last_in_range - last_too_large
    return total
