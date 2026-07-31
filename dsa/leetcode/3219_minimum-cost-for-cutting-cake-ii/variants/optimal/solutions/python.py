def solve(m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
    horizontal = sorted(horizontalCut, reverse=True)
    vertical = sorted(verticalCut, reverse=True)
    i = j = 0
    horizontal_pieces = vertical_pieces = 1
    total = 0
    while i < len(horizontal) and j < len(vertical):
        if horizontal[i] >= vertical[j]:
            total += horizontal[i] * vertical_pieces
            horizontal_pieces += 1
            i += 1
        else:
            total += vertical[j] * horizontal_pieces
            vertical_pieces += 1
            j += 1
    total += sum(horizontal[i:]) * vertical_pieces
    total += sum(vertical[j:]) * horizontal_pieces
    return total
