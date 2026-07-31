def solve(n: int) -> bool:
    adjacent_pairs = n & (n >> 1)
    return adjacent_pairs != 0 and (adjacent_pairs & (adjacent_pairs - 1)) == 0
