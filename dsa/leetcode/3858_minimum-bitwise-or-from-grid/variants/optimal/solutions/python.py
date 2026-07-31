def solve(grid: list[list[int]]) -> int:
    forbidden_bits = 0
    result = 0
    highest_bit = max(max(row) for row in grid).bit_length() - 1

    for bit in range(highest_bit, -1, -1):
        candidate_forbidden = forbidden_bits | (1 << bit)

        if all(
            any((value & candidate_forbidden) == 0 for value in row)
            for row in grid
        ):
            forbidden_bits = candidate_forbidden
        else:
            result |= 1 << bit

    return result
