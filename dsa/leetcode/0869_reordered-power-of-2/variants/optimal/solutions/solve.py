def digit_signature(value):
    counts = [0] * 10
    while value:
        counts[value % 10] += 1
        value //= 10
    return tuple(counts)


POWER_OF_TWO_SIGNATURES = {digit_signature(1 << exponent) for exponent in range(34)}


def solve(n):
    return digit_signature(n) in POWER_OF_TWO_SIGNATURES
