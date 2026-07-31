def solve(n: int) -> int:
    reversed_n = 0
    remaining = n

    while remaining:
        reversed_n = reversed_n * 10 + remaining % 10
        remaining //= 10

    return abs(n - reversed_n)
