"""Optimal app-local solution for LeetCode 1510."""


def solve(n: int) -> bool:
    """Return whether the first player wins by removing square counts."""
    squares = [value * value for value in range(1, int(n**0.5) + 1)]
    winning = bytearray(n + 1)
    for stones in range(1, n + 1):
        for square in squares:
            if square > stones:
                break
            if not winning[stones - square]:
                winning[stones] = 1
                break
    return bool(winning[n])
