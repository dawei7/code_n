"""Optimal solution for bit_08: Divide Without /.

Repeated subtraction: dividend = divisor * quotient + remainder.
Build the quotient bit-by-bit from the most significant bit
of the divisor. Use absolute values; handle the sign at the end.
"""


def solve(dividend, divisor):
    if divisor == 0:
        return 0
    if dividend == 0:
        return 0
    negative = (dividend < 0) != (divisor < 0)
    a = abs(dividend)
    b = abs(divisor)
    quotient = 0
    power = 32
    while (b << power) > a:
        power -= 1
    while power >= 0:
        if (b << power) <= a:
            a -= b << power
            quotient |= 1 << power
        power -= 1
    if negative:
        quotient = -quotient
    return quotient
