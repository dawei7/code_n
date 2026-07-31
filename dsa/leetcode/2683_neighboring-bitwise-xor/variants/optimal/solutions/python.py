def solve(derived: list[int]) -> bool:
    parity = 0
    for value in derived:
        parity ^= value
    return parity == 0
