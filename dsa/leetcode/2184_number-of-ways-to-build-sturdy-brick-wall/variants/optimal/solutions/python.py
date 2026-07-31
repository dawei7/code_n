def solve(height: int, width: int, bricks: list[int]) -> int:
    modulus = 1_000_000_007
    row_masks = []

    def build_row(position: int, seams: int) -> None:
        for brick in bricks:
            next_position = position + brick
            if next_position > width:
                continue
            if next_position == width:
                row_masks.append(seams)
            else:
                build_row(next_position, seams | (1 << next_position))

    build_row(0, 0)
    compatible = [
        [previous for previous, other in enumerate(row_masks) if mask & other == 0]
        for mask in row_masks
    ]

    ways = [1] * len(row_masks)
    for _ in range(1, height):
        ways = [
            sum(ways[previous] for previous in predecessors) % modulus
            for predecessors in compatible
        ]

    return sum(ways) % modulus
