def solve(nums: list[int]) -> int:
    squares = sorted(value * value for value in nums)
    negative_count = len(squares) // 2
    return sum(squares[negative_count:]) - sum(squares[:negative_count])
