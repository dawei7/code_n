def solve(p: int) -> int:
    modulus = 1_000_000_007
    maximum = (1 << p) - 1
    pair_count = (1 << (p - 1)) - 1
    return maximum % modulus * pow(maximum - 1, pair_count, modulus) % modulus
