def solve(left: int, right: int) -> int:
    prime_counts = {2, 3, 5, 7, 11, 13, 17, 19}
    return sum(value.bit_count() in prime_counts for value in range(left, right + 1))
