from typing import List


def solve(upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
    top = [0] * len(colsum)
    bottom = [0] * len(colsum)
    for i, value in enumerate(colsum):
        if value == 2:
            top[i] = bottom[i] = 1
            upper -= 1
            lower -= 1
    if upper < 0 or lower < 0:
        return []
    for i, value in enumerate(colsum):
        if value == 1:
            if upper > lower:
                top[i] = 1
                upper -= 1
            else:
                bottom[i] = 1
                lower -= 1
    return [top, bottom] if upper == 0 and lower == 0 else []
