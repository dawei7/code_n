from math import comb


def solve(k: int) -> int:
    total = 0
    jump = 0
    while (downs := (1 << jump) - k) <= jump + 1:
        if downs >= 0:
            total += comb(jump + 1, downs)
        jump += 1
    return total
