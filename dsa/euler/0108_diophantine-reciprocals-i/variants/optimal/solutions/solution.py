def count_solutions_n2(n: int) -> int:
    """Compute number of distinct solutions to 1/x + 1/y = 1/n via prime factorization of n^2."""
    temp = n
    divisors_n2 = 1
    d = 2

    while d * d <= temp:
        if temp % d == 0:
            exp = 0
            while temp % d == 0:
                exp += 1
                temp //= d
            divisors_n2 *= (2 * exp + 1)
        d += 1

    if temp > 1:
        divisors_n2 *= 3  # (2 * 1 + 1)

    return (divisors_n2 + 1) // 2


def solve(target: int = 1000) -> int:
    """Find least n for which number of distinct solutions to 1/x + 1/y = 1/n exceeds target.
    
    Time Complexity: O(N * sqrt(N))
    Space Complexity: O(1)
    """
    n = 1
    while True:
        if count_solutions_n2(n) > target:
            return n
        n += 1
