def solve(groups: list[int], elements: list[int]) -> list[int]:
    max_group = max(groups)
    first_index = {}
    for index, value in enumerate(elements):
        if value <= max_group and value not in first_index:
            first_index[value] = index

    best_for_value = [10**9] * (max_group + 1)
    for value, index in first_index.items():
        for multiple in range(value, max_group + 1, value):
            if index < best_for_value[multiple]:
                best_for_value[multiple] = index

    return [-1 if best_for_value[group] == 10**9 else best_for_value[group] for group in groups]
