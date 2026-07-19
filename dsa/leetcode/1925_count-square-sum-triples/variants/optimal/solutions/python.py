def solve(n: int) -> int:
    hypotenuse_squares = {value * value for value in range(1, n + 1)}
    return sum(
        first * first + second * second in hypotenuse_squares
        for first in range(1, n + 1)
        for second in range(1, n + 1)
    )
