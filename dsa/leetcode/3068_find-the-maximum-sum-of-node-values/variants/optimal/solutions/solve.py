def solve(nums: list[int], k: int, edges: list[list[int]]) -> int:
    best_sum = 0
    beneficial_toggles = 0
    smallest_adjustment = float("inf")

    for value in nums:
        toggled = value ^ k
        best_sum += max(value, toggled)
        beneficial_toggles += int(toggled > value)
        smallest_adjustment = min(smallest_adjustment, abs(toggled - value))

    if beneficial_toggles % 2 == 1:
        best_sum -= smallest_adjustment

    return best_sum
