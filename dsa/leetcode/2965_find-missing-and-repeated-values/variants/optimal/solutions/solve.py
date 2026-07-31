from typing import List


def solve(grid: List[List[int]]) -> List[int]:
    n = len(grid)
    limit = n * n
    observed_sum = 0
    observed_square_sum = 0

    for row in grid:
        for value in row:
            observed_sum += value
            observed_square_sum += value * value

    expected_sum = limit * (limit + 1) // 2
    expected_square_sum = limit * (limit + 1) * (2 * limit + 1) // 6
    difference = observed_sum - expected_sum
    pair_sum = (observed_square_sum - expected_square_sum) // difference
    repeated = (difference + pair_sum) // 2
    missing = pair_sum - repeated
    return [repeated, missing]
