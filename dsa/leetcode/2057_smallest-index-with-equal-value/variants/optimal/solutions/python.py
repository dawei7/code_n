def solve(nums: list[int]) -> int:
    for index, value in enumerate(nums):
        if index % 10 == value:
            return index
    return -1
