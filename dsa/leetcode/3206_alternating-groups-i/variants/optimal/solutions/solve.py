def solve(colors: list[int]) -> int:
    size = len(colors)
    return sum(
        colors[index] != colors[index - 1] and colors[index] != colors[(index + 1) % size] for index in range(size)
    )
