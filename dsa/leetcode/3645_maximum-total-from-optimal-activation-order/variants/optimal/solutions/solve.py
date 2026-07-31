def solve(value: list[int], limit: list[int]) -> int:
    elements = sorted(zip(limit, value), key=lambda item: (item[0], -item[1]))
    total = 0
    current_limit = -1
    selected = 0

    for element_limit, element_value in elements:
        if element_limit != current_limit:
            current_limit = element_limit
            selected = 0
        if selected < element_limit:
            total += element_value
            selected += 1

    return total
