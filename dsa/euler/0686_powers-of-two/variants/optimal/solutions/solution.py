"""Project Euler Problem 686: Powers of Two.

Mathematical Formulation:
p(L, n) is the n-th exponent j such that 2^j starts with the decimal digits L.
Find p(123, 678910).
Evaluated via floating point fractional part { j * log10(2) }.
"""

from __future__ import annotations

import math


def solve(target_prefix: str = "123", target_count: int = 678910) -> str:
    """Compute p(123, 678910) in pure Python."""
    log10_2 = math.log10(2)
    low = math.log10(1.23)
    high = math.log10(1.24)
    
    count = 0
    j = 1
    frac = 0.0
    
    while count < target_count:
        frac += log10_2
        if frac >= 1.0:
            frac -= 1.0
        if low <= frac < high:
            count += 1
            if count == target_count:
                return str(j)
        j += 1
        
    return str(j)


if __name__ == "__main__":
    print(solve())
