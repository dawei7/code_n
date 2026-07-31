def solve(nums: list[int], limit: int, goal: int) -> int:
    difference = abs(goal - sum(nums))
    return (difference + limit - 1) // limit
