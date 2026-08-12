import math


def solve(limit: int = 10**15) -> int:
    """Find the sum of all f(m, n) <= 10^15 for m >= 2, n >= 1 using Burnside's Lemma.
    
    Time Complexity: O(m_max * n_max * log(n_max))
    Space Complexity: O(1)
    """

    def phi(n):
        res = n
        p = 2
        temp = n
        while p * p <= temp:
            if temp % p == 0:
                while temp % p == 0:
                    temp //= p
                res -= res // p
            p += 1
        if temp > 1:
            res -= res // temp
        return res

    def f(m, n):
        tot = 0
        for d in range(1, n + 1):
            if n % d == 0:
                phi_val = phi(n // d)
                num = math.factorial(m * d)
                den = (math.factorial(d)) ** m
                tot += phi_val * (num // den)
        return tot // (m * n)

    total_sum = 0
    m = 2
    while True:
        if f(m, 1) > limit:
            break
        n = 1
        while True:
            val = f(m, n)
            if val > limit:
                break
            total_sum += val
            n += 1
        m += 1

    return total_sum
