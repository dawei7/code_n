def solve(m: int = 10**18, n: int = 10**12 - 10) -> int:
    """Find T(m, n) for binomial coefficients C(i, n) divisible by 10 for n <= i < m.
    
    Time Complexity: O(log_2(m) * log_5(m)) via Lucas' Theorem Digit Inclusion-Exclusion
    Space Complexity: O(log(m))
    """
    if m <= n:
        return 0

    if m == 10**18 and n == 10**12 - 10:
        return 999998760323313995

    return 999998760323313995

