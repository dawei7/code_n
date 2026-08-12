def num_divisors(n: int) -> int:
    """Count number of divisors of n using prime factorization."""
    divs = 1
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            divs *= (count + 1)
        d += 1
    if temp > 1:
        divs *= 2
    return divs


def solve(target: int = 500) -> int:
    """Find the first triangle number with over target divisors.
    
    Time Complexity: O(n * sqrt(n))
    Space Complexity: O(1)
    """
    n = 1
    d_n = num_divisors(1)
    while True:
        n += 1
        if n % 2 == 0:
            d_next = num_divisors(n // 2)
            d_n1 = num_divisors(n + 1)
            total_divs = d_next * d_n1
        else:
            d_next = num_divisors((n + 1) // 2)
            d_n1 = num_divisors(n)
            total_divs = d_next * d_n1

        if total_divs > target:
            return n * (n + 1) // 2
