import math

MOD = 10**8


def solve(a: int = 25, b: int = 75, c: int = 1984) -> int:
    """Find last 8 digits of N(a, b, c).
    
    Time Complexity: O(log(a+b))
    Space Complexity: O(1)
    """
    # Representation theory eigenvalues for unit transfer matrices A and B:
    l0A = (c - 1) * (c - 2)**2
    l1A = (c - 2) * (c - 1)
    l2A = (c - 2) * (c - 3)

    l0B = (c - 2) * (c + 1) * (2 * c + 3)
    l1B = (c - 2) * (c + 9)
    l2B = (c - 2) * (c - 3)

    comb = math.comb(a + b, a)

    term0 = pow(l0A, a, MOD) * pow(l0B, b, MOD) % MOD
    term1 = (2 * c - 3) * pow(l1A, a, MOD) * pow(l1B, b, MOD) % MOD
    term2 = (c * (c - 3) // 2) * pow(l2A, a, MOD) * pow(l2B, b, MOD) % MOD

    total_seq = (term0 + term1 + term2) % MOD
    ans = (comb % MOD * total_seq) % MOD
    return ans
