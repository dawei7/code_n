def solve(nums: list[int]) -> list[int]:
    return [
        -1 if number == 2 else number ^ (((number + 1) & -(number + 1)) >> 1)
        for number in nums
    ]
