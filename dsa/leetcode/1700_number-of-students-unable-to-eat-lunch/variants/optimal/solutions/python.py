def solve(students: list[int], sandwiches: list[int]) -> int:
    remaining = [0, 0]
    for preference in students:
        remaining[preference] += 1

    for index, sandwich in enumerate(sandwiches):
        if remaining[sandwich] == 0:
            return len(sandwiches) - index
        remaining[sandwich] -= 1

    return 0
