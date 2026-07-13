def solve(n: int, k: int) -> int:
    del n
    position = k - 1
    symbol = 0
    while position:
        symbol ^= position & 1
        position >>= 1
    return symbol
