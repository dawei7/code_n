def solve(nums, s, d):
    positions = sorted(
        position + d if direction == "R" else position - d
        for position, direction in zip(nums, s)
    )

    total = 0
    prefix = 0
    for index, position in enumerate(positions):
        total += index * position - prefix
        prefix += position

    return total % 1_000_000_007
