def solve(arrays: list[list[int]]) -> list[int]:
    frequencies = [0] * 101
    for array in arrays:
        for value in array:
            frequencies[value] += 1

    required = len(arrays)
    return [
        value
        for value in range(1, 101)
        if frequencies[value] == required
    ]
