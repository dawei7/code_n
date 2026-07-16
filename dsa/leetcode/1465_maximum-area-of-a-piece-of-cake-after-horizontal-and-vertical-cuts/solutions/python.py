def solve(h, w, horizontal_cuts, vertical_cuts):
    horizontal = [0, *sorted(horizontal_cuts), h]
    vertical = [0, *sorted(vertical_cuts), w]

    max_height = max(
        horizontal[index] - horizontal[index - 1]
        for index in range(1, len(horizontal))
    )
    max_width = max(
        vertical[index] - vertical[index - 1]
        for index in range(1, len(vertical))
    )

    return (max_height * max_width) % 1_000_000_007
