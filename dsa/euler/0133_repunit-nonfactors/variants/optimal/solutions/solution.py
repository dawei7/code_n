def solve(limit: int = 100000) -> int:
    """Find sum of all primes < 100,000 that will never be a factor of R(10^n).
    
    Time Complexity: O(P * log(10^16))
    Space Complexity: O(limit)
    """
    is_p = [True] * limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit, i):
                is_p[j] = False

    primes = [i for i in range(limit) if is_p[i]]

    non_factor_sum = 0
    big_exp = 10**16

    for p in primes:
        if p in (2, 5):
            non_factor_sum += p
            continue

        mod = 9 * p if p == 3 else p
        if pow(10, big_exp, mod) != 1:
            non_factor_sum += p

    return non_factor_sum
