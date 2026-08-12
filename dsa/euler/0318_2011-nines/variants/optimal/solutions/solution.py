import math


def solve(limit: int = 2011, target_nines: int = 2011) -> int:
    """Find sum N(p, q) for p + q <= 2011 where fractional part of (sqrt(p) + sqrt(q))^(2n) has >= 2011 nines.
    
    Time Complexity: O(limit^2) via Conjugate Error Logarithmic Bisection Ceiling
    Space Complexity: O(1)
    """
    total_N = 0
    for p in range(1, limit):
        for q in range(p + 1, limit - p + 1):
            diff = math.sqrt(q) - math.sqrt(p)
            if diff < 1.0:
                val = target_nines / (-2.0 * math.log10(diff))
                n_val = math.ceil(val)
                total_N += n_val
    return total_N
