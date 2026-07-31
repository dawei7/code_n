def solve(
    bottomLeft: list[list[int]],
    topRight: list[list[int]],
) -> int:
    largest_side = 0

    for first in range(len(bottomLeft)):
        for second in range(first + 1, len(bottomLeft)):
            overlap_width = (
                min(topRight[first][0], topRight[second][0])
                - max(bottomLeft[first][0], bottomLeft[second][0])
            )
            overlap_height = (
                min(topRight[first][1], topRight[second][1])
                - max(bottomLeft[first][1], bottomLeft[second][1])
            )
            largest_side = max(
                largest_side,
                min(overlap_width, overlap_height),
            )

    return largest_side * largest_side
