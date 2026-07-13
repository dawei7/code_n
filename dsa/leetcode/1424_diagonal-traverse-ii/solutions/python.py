from collections import defaultdict


def solve(nums):
    diagonals = defaultdict(list)
    for row, values in enumerate(nums):
        if not isinstance(values, list):
            values = [values]
        for col, value in enumerate(values):
            diagonals[row + col].append(value)
    result = []
    for key in sorted(diagonals):
        result.extend(reversed(diagonals[key]))
    return result
