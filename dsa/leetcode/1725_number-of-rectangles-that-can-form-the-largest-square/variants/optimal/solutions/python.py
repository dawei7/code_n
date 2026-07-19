def solve(rectangles: list[list[int]]) -> int:
    best_side = 0
    count = 0

    for length, width in rectangles:
        side = min(length, width)
        if side > best_side:
            best_side = side
            count = 1
        elif side == best_side:
            count += 1

    return count
