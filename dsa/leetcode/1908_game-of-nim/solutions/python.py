def solve(piles: list[int]) -> bool:
    nim_sum = 0
    for stones in piles:
        nim_sum ^= stones
    return nim_sum != 0
