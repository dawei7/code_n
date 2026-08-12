def sum_proper_divisors(n: int) -> int:
    """Sum of proper divisors of n."""
    if n <= 1:
        return 0
    total = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            total += d
            if d * d != n:
                total += n // d
        d += 1
    return total


def solve(limit: int = 10000) -> int:
    """Evaluate sum of all amicable numbers under limit.
    
    Time Complexity: O(limit * sqrt(limit))
    Space Complexity: O(limit)
    """
    d_vals = [sum_proper_divisors(i) for i in range(limit)]
    amicable_sum = 0
    for a in range(1, limit):
        b = d_vals[a]
        if b != a and b < limit and d_vals[b] == a:
            amicable_sum += a
    return amicable_sum
