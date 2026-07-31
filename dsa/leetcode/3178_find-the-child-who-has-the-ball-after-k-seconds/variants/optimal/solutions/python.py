def solve(n: int, k: int) -> int:
    period = 2 * (n - 1)
    offset = k % period

    if offset < n:
        return offset

    return period - offset
