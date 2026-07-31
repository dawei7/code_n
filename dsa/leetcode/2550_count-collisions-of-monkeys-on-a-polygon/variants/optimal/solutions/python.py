def solve(n: int) -> int:
    modulus = 1_000_000_007
    return (pow(2, n, modulus) - 2) % modulus
