def solve(list1: list[str], list2: list[str]) -> list[str]:
    """Return all common strings with the minimum index sum."""
    first_indices = {
        value: index
        for index, value in enumerate(list1)
    }
    best_sum = float("inf")
    answers: list[str] = []

    for second_index, value in enumerate(list2):
        first_index = first_indices.get(value)
        if first_index is None:
            continue

        index_sum = first_index + second_index
        if index_sum < best_sum:
            best_sum = index_sum
            answers = [value]
        elif index_sum == best_sum:
            answers.append(value)

    return answers

