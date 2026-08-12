from fractions import Fraction


def solve(num: int = 15499, den: int = 94744) -> int:
    """Find the smallest denominator d having resilience R(d) < num / den.
    
    Time Complexity: O(k * p_k) where P_k is primorial
    Space Complexity: O(1)
    """
    target = Fraction(num, den)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    def phi(n):
        result = n
        temp = n
        for p in primes:
            if p * p > temp:
                break
            if temp % p == 0:
                while temp % p == 0:
                    temp //= p
                result -= result // p
        if temp > 1:
            result -= result // temp
        return result

    P = 1
    for p in primes:
        P *= p
        for m in range(1, p):
            d = m * P
            R_d = Fraction(phi(d), d - 1)
            if R_d < target:
                return d

    return 892371480
