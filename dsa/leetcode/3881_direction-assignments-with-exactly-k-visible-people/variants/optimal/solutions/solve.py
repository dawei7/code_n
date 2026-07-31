def solve(n: int, pos: int, k: int) -> int:
    mod = 1_000_000_007
    available = n - 1
    selected = min(k, available - k)
    numerator = 1
    denominator = 1

    for offset in range(1, selected + 1):
        numerator = numerator * (available - selected + offset) % mod
        denominator = denominator * offset % mod

    combinations = numerator * pow(denominator, mod - 2, mod) % mod
    return 2 * combinations % mod
