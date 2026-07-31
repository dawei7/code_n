from math import log10


def solve(left: int, right: int) -> str:
    modulus = 10**12
    suffix = 1
    leading = 1.0
    zeros = 0
    logarithm = 0.0
    compensation = 0.0

    for value in range(left, right + 1):
        increment = log10(value) - compensation
        updated = logarithm + increment
        compensation = (updated - logarithm) - increment
        logarithm = updated

        leading *= value
        while leading >= modulus:
            leading /= 10

        suffix *= value
        while suffix % 10 == 0:
            suffix //= 10
            zeros += 1
        suffix %= modulus

    significant_log = logarithm - zeros
    if significant_log < 10:
        return f"{suffix}e{zeros}"

    while leading >= 100000:
        leading /= 10
    return f"{int(leading)}...{suffix % 100000:05d}e{zeros}"
