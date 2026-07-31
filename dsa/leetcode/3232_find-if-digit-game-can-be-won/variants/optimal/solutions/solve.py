def solve(nums: list[int]) -> bool:
    balance = 0
    for value in nums:
        balance += value if value < 10 else -value
    return balance != 0
