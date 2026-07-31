def solve(nums: list[int]) -> int:
    total = sum(nums)
    prefix = 0
    best_index = 0
    best_difference = float("inf")

    for index, value in enumerate(nums):
        prefix += value
        left_average = prefix // (index + 1)
        remaining = len(nums) - index - 1
        right_average = (total - prefix) // remaining if remaining else 0
        difference = abs(left_average - right_average)
        if difference < best_difference:
            best_difference = difference
            best_index = index

    return best_index
