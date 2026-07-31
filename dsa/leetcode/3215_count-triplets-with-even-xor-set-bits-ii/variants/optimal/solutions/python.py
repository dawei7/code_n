def solve(a: list[int], b: list[int], c: list[int]) -> int:
    def parity_counts(values: list[int]) -> tuple[int, int]:
        odd = sum(value.bit_count() & 1 for value in values)
        return len(values) - odd, odd

    a_even, a_odd = parity_counts(a)
    b_even, b_odd = parity_counts(b)
    c_even, c_odd = parity_counts(c)

    return (
        a_even * b_even * c_even
        + a_even * b_odd * c_odd
        + a_odd * b_even * c_odd
        + a_odd * b_odd * c_even
    )
