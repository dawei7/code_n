from functools import lru_cache
import math


@lru_cache(maxsize=None)
def sum_g_floor(M: int) -> int:
    """Hyperbola method to compute sum_{g=1}^M g * floor(M / g)."""
    tot = 0
    l = 1
    while l <= M:
        k = M // l
        r = M // k
        sum_g = (r * (r + 1) - (l - 1) * l) // 2
        tot += sum_g * k
        l = r + 1
    return tot


def solve(N: int = 100000000) -> int:
    """Find sum of real parts of all Gaussian integer divisors of n for 1 <= n <= N.
    
    Time Complexity: O(N * sqrt(N_unique_norms))
    Space Complexity: O(Unique_Norms)
    """
    total_sum = sum_g_floor(N)

    max_A = int(math.isqrt(N // 2))
    for A in range(1, max_A + 1):
        A2 = A * A
        max_B = int(math.isqrt(N - A2))
        for B in range(A, max_B + 1):
            if math.gcd(A, B) != 1:
                continue
            norm = A2 + B * B
            if A == B:
                F = 2 * A
            else:
                F = 2 * (A + B)

            total_sum += F * sum_g_floor(N // norm)

    return total_sum
