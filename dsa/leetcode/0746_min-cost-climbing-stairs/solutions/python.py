def solve(cost: list[int]) -> int:
    two_before = 0
    one_before = 0

    for step_cost in cost:
        current = step_cost + min(two_before, one_before)
        two_before, one_before = one_before, current

    return min(two_before, one_before)
