from collections import Counter
from math import gcd


def solve(rectangles: list[list[int]]) -> int:
    frequencies = Counter()
    pairs = 0

    for width, height in rectangles:
        divisor = gcd(width, height)
        ratio = (width // divisor, height // divisor)
        pairs += frequencies[ratio]
        frequencies[ratio] += 1

    return pairs
