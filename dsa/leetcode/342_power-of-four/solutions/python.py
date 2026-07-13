EVEN_BIT_POSITIONS = 0x55555555


def solve(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0 and (n & EVEN_BIT_POSITIONS) != 0
