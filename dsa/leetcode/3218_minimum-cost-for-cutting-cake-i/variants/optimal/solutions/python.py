def solve(m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
    horizontal = sorted(horizontalCut, reverse=True)
    vertical = sorted(verticalCut, reverse=True)
    horizontal_index = vertical_index = 0
    horizontal_pieces = vertical_pieces = 1
    total = 0

    while horizontal_index < len(horizontal) and vertical_index < len(vertical):
        if horizontal[horizontal_index] >= vertical[vertical_index]:
            total += horizontal[horizontal_index] * vertical_pieces
            horizontal_pieces += 1
            horizontal_index += 1
        else:
            total += vertical[vertical_index] * horizontal_pieces
            vertical_pieces += 1
            vertical_index += 1

    total += sum(horizontal[horizontal_index:]) * vertical_pieces
    total += sum(vertical[vertical_index:]) * horizontal_pieces
    return total
