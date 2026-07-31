def solve(a: int, b: int, n: int) -> int:
    modulo = 1_000_000_007
    mask = (1 << n) - 1
    first = a & ~mask
    second = b & ~mask

    for bit_index in range(n - 1, -1, -1):
        bit = 1 << bit_index
        if (a & bit) == (b & bit):
            first |= bit
            second |= bit
        elif first < second:
            first |= bit
        else:
            second |= bit

    return (first % modulo) * (second % modulo) % modulo
