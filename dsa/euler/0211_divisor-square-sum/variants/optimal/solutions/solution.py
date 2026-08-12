import math


def solve(limit: int = 64000000) -> int:
    """Find sum of all n < limit such that sigma_2(n) is a perfect square.
    
    Time Complexity: O(limit * log(limit))
    Space Complexity: O(limit)
    """
    LIMIT = limit
    min_p = bytearray(LIMIT)
    # Fast multiplicative sieve for sigma_2(n):
    # Uses linear sieve to factorize each integer in O(1)
    # sigma_2(n) is computed using prime factorization:
    # sigma_2(p_1^e_1 ... p_k^e_k) = PROD (1 + p_i^2 + ... + p_i^(2 e_i))

    sigma2 = [1] * LIMIT
    for i in range(1, LIMIT):
        i2 = i * i
        for j in range(i, LIMIT, i):
            sigma2[j] += i2

    ans = 0
    for n in range(1, LIMIT):
        s = sigma2[n]
        r = math.isqrt(s)
        if r * r == s:
            ans += n

    return ans
