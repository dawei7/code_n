def solve(nums: list[int], k: int) -> int:
    values = sorted(nums, reverse=True)
    total = sum(values[:k])
    if total % 2 == 0:
        return total

    smallest_selected: list[int | None] = [None, None]
    for value in values[:k]:
        smallest_selected[value % 2] = value

    largest_unselected: list[int | None] = [None, None]
    for value in values[k:]:
        parity = value % 2
        if largest_unselected[parity] is None:
            largest_unselected[parity] = value

    best = -1
    for selected_parity in (0, 1):
        selected = smallest_selected[selected_parity]
        replacement = largest_unselected[1 - selected_parity]
        if selected is not None and replacement is not None:
            best = max(best, total - selected + replacement)
    return best
