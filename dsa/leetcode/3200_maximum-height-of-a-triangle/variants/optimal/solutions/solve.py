from math import isqrt


def solve(red: int, blue: int) -> int:
    def height(first: int, second: int) -> int:
        odd_rows = isqrt(first)
        even_rows = (isqrt(1 + 4 * second) - 1) // 2
        return min(2 * odd_rows, 2 * even_rows + 1)

    return max(height(red, blue), height(blue, red))
