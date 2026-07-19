def solve(nums: list[int], limit: int, goal: int) -> int:
    current_sum = 0
    for value in nums:
        current_sum += value
    difference = abs(goal - current_sum)
    return (difference + limit - 1) // limit
