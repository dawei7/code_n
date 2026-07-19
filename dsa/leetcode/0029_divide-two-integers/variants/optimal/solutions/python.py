def solve(dividend: int, divisor: int) -> int:
    negative = (dividend < 0) != (divisor < 0)
    remainder = abs(dividend)
    divisor_magnitude = abs(divisor)
    quotient = 0

    for shift in range(max(0, remainder.bit_length() - divisor_magnitude.bit_length()), -1, -1):
        shifted = divisor_magnitude << shift
        if shifted <= remainder:
            remainder -= shifted
            quotient |= 1 << shift

    if negative:
        quotient = -quotient
    return min(2**31 - 1, max(-(2**31), quotient))
