def _xor_prefix(value):
    if value < 0:
        return 0

    remainder = value & 3
    if remainder == 0:
        return value
    if remainder == 1:
        return 1
    if remainder == 2:
        return value + 1
    return 0


def solve(n, start):
    first = start >> 1
    high_bits = _xor_prefix(first - 1) ^ _xor_prefix(first + n - 1)
    low_bit = (start & 1) if n & 1 else 0
    return (high_bits << 1) | low_bit
