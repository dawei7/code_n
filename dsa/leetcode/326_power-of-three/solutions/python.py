MAXIMUM_POWER_OF_THREE = 1_162_261_467


def solve(n: int) -> bool:
    return n > 0 and MAXIMUM_POWER_OF_THREE % n == 0
