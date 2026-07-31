def solve(rings: str) -> int:
    color_bit = {"R": 1, "G": 2, "B": 4}
    rods = [0] * 10

    for index in range(0, len(rings), 2):
        color = rings[index]
        rod = int(rings[index + 1])
        rods[rod] |= color_bit[color]

    return sum(mask == 7 for mask in rods)
