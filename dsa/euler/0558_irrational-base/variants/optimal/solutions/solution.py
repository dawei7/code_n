"""Project Euler Problem 558: Irrational Base.

Find S(5000000), where S(m) = sum_{j=1..m} w(j^2), and w(n) is the number of terms
in the unique greedy canonical base-r representation (x^3 = x^2 + 1).
"""

from decimal import Decimal, ROUND_FLOOR, localcontext
from typing import List, Tuple

SCALE = 10**90
DECIMAL_PRECISION = 150
MIN_EXPONENT = -200
MAX_EXPONENT = 128


def _base_root() -> Decimal:
    x = Decimal(3) / Decimal(2)
    for _ in range(24):
        x -= (x * x * x - x * x - 1) / (3 * x * x - 2 * x)
    return +x


def _build_scaled_powers() -> Tuple[List[int], int]:
    with localcontext() as ctx:
        ctx.prec = DECIMAL_PRECISION
        r = _base_root()
        values = {0: Decimal(1), 1: r, 2: r * r}

        for exponent in range(2, MAX_EXPONENT):
            values[exponent + 1] = values[exponent] + values[exponent - 2]
        for offset in range(1, -MIN_EXPONENT + 1):
            values[-offset] = values[-offset + 3] - values[-offset + 2]

        decimal_scale = Decimal(SCALE)
        powers = [
            int(
                (values[exponent] * decimal_scale).to_integral_value(
                    rounding=ROUND_FLOOR
                )
            )
            for exponent in range(MIN_EXPONENT, MAX_EXPONENT + 1)
        ]

    return powers, -MIN_EXPONENT


def solve(limit: int = 5_000_000) -> int:
    """Compute S(limit) using high-precision integer scaled powers and monotonic greedy subtraction."""
    powers, zero_index = _build_scaled_powers()

    lead = zero_index
    square = 0
    odd_increment = SCALE
    two = 2 * SCALE
    total = 0
    power_count = len(powers)

    for _ in range(limit):
        square += odd_increment
        odd_increment += two

        while lead + 1 < power_count and powers[lead + 1] <= square:
            lead += 1

        residual = square - powers[lead]
        terms = 1
        pos = lead - 3

        while pos >= 0:
            while pos >= 0 and powers[pos] > residual:
                pos -= 1
            if pos < 0:
                break
            residual -= powers[pos]
            terms += 1
            pos -= 3

        total += terms

    return total


if __name__ == "__main__":
    print(solve())
